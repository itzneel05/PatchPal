"use client";

import useSWR from "swr";

interface FriendProfile {
  name: string;
  tech_stack: string[];
  severity_threshold: string;
}

const fetcher = (url: string) => fetch(url).then((r) => r.json());

export function useProfile() {
  return useSWR<FriendProfile, Error>("http://localhost:8000/api/profile", fetcher);
}
