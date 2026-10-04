"use client";

import useSWR from "swr";
import { useEffect, useState } from "react";

interface Vulnerability {
  cve_id?: string;
  title: string;
  severity: string;
  affected_tech?: string[];
  source_url: string;
  published: string;
  raw_description: string;
}

interface Digest {
  friend_name: string;
  date_generated: string;
  vulnerabilities: Vulnerability[];
  ai_summary: string;
}

/**
 * SWR hook to fetch the digest from the FastAPI backend.
 * Revalidates on focus and every 60 seconds.
 */
export function useDigest() {
  const { data, error, isLoading, mutate } = useSWR<
    Digest,
    Error
  >("http://localhost:8000/api/digest", fetcher, {
    revalidateOnFocus: true,
    revalidateIfStale: true,
    refreshInterval: 60000, // 1 minute
    shouldRetryOnError: true,
  });

  // State for optimistic UI or loading indicators
  const [localState, setLocalState] = useState({
    data: data,
    isLoading,
    isError: !!error,
  });

  // Sync remote state to local state
  useEffect(() => {
    setLocalState({
      data: data,
      isLoading,
      isError: !!error,
    });
  }, [data, error]);

  return {
    data: localState.data,
    isLoading: localState.isLoading,
    isError: localState.isError,
    error,
    mutate,
  };
}

/**
 * Simple fetcher function for SWR
 */
async function fetcher(url: string) {
  const res = await fetch(url, {
    // Cache strategy: force cache for now, but revalidate on focus
    // In production you might want to add credentials if needed
    headers: {
      "Accept": "application/json",
    },
    // Don't include credentials by default unless needed
  });

  if (!res.ok) {
    const errorData = await res.json().catch(() => ({}));
    throw new Error(errorData.detail || "Failed to fetch digest");
  }

  return res.json();
}

export type { Digest, Vulnerability };
