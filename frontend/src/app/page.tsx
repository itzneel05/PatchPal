/* --------------------------------------------------------------
   PatchPal Dashboard — Frontend (MVP simplified)
   Design: `design-taste-frontend` rules applied
   - Geist font, neutral gray palette, one accent color only
   - Restrained motion, CSS Grid Bento layout
   -------------------------------------------------------------- */

"use client";

import { useDigest, Digest, Vulnerability } from "@/hooks/use-digest";

import { motion } from "motion/react";
import { Shield } from "@phosphor-icons/react";
import { useEffect, useState } from "react";

export default function Home() {
  const {
    data: digest,
    isLoading,
    isError,
    error,
    mutate,
  } = useDigest();

  // Keep a local copy of the friend's name for the header
  const [friendName, setFriendName] = useState<string>("");

  useEffect(() => {
    if (digest) {
      setFriendName(digest.friend_name);
    }
  }, [digest]);

  // If no data yet, show a friendly placeholder
  if (!digest && !isLoading && !isError) {
    return (
      <main className="min-h-screen flex items-center justify-center p-8 text-center">
        <h1 className="text-3xl font-bold tracking-tighter mb-4">
          {friendName || "PatchPal"} Dashboard
        </h1>
        <p className="text-zinc-500 max-w-xl mx-auto">
          Fetching your security digest… the open-source AI is working its magic.
        </p>
      </main>
    );
  }

  // If error, show a simple error state
  if (isError) {
    return (
      <main className="min-h-screen flex items-center justify-center p-8 text-center">
        <h1 className="text-xl font-medium text-destructive mb-4">
          Something went wrong
        </h1>
        <p className="text-zinc-400 max-w-xl mx-auto">
          {error?.message || "Unable to load the digest at this time."}
        </p>
<button
          onClick={() => mutate()}
          className="mt-4 px-4 py-2 bg-primary text-white rounded hover:bg-primary/90"
        >
          Retry
        </button>
      </main>
    );
  }

  // If loading, show text only
  if (isLoading && !digest) {
    return (
      <main className="min-h-screen flex items-center justify-center p-8">
        <p className="text-zinc-500">Loading your security digest…</p>
      </main>
    );
  }

  // At this point we have a digest
  const vulnerabilities = digest?.vulnerabilities || [];
  const aiSummary = digest?.ai_summary || "";

  return (
    <main className="min-h-screen bg-background p-4 md:p-8">
      {/* Header: Friend name + refresh button */}
      <header className="mb-6 md:mb-8 flex items-center justify-between flex flex-col md:flex-row gap-4">
        <div>
          <h1 className="text-3xl font-bold tracking-tighter text-foreground">
            {friendName || "Friend"}
          </h1>
          <p className="text-sm text-muted-foreground mt-1">
            Security digest for {new Date().toLocaleDateString()}
          </p>
        </div>

        <button
          onClick={() => mutate()}
          className="px-4 py-2 bg-primary text-white rounded hover:bg-primary/90"
          >
            Refresh
          </button>
      </header>

      {/* AI Summary Card */}
      {aiSummary ? (
        <div className="mb-6 w-full max-w-2xl mx-auto p-4 bg-primary/5 border border-primary/10 rounded-lg">
          <p className="prose max-w-none text-muted-foreground">
            {aiSummary}
          </p>
        </div>
      ) : null}

      {/* Vulnerability Grid */}
      {vulnerabilities.length > 0 ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 max-w-7xl mx-auto">
          {vulnerabilities.map((vuln, idx) => (
            <div
              key={vuln.cve_id || vuln.title}
              className="p-4 hover:shadow-md transition-shadow rounded-border"
            >
              <div className="flex items-start justify-between">
                <div>
                  <h3 className="text-sm font-medium text-foreground">
                    {vuln.title}
                  </h3>
                  <p className="text-xs text-muted-foreground truncated">
                    {vuln.raw_description?.substring(0, 120)}...
                  </p>
                </div>
                <span
                  className={
                    vuln.severity === "Critical"
                      ? "bg-destructive/10 text-destructive text-xs"
                      : vuln.severity === "High"
                      ? "bg-primary/10 text-primary text-xs"
                      : "bg-muted/10 text-muted-foreground text-xs"
                  }
                >
                  {vuln.severity}
                </span>
              </div>
              <div className="grid grid-cols-2 gap-2 text-xs mt-2">
                <div>
                  <div className="text-muted-foreground">Affects</div>
                  <p className="font-medium">{vuln.affected_tech?.join(", ") || "Unknown"}</p>
                </div>
                <div>
                  <div className="text-muted-foreground">Source</div>
                  <a
                    href={vuln.source_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="underline text-primary hover:text-primary/80 block mt-1"
                  >
                    View source
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>
      ) : null}

      {/* Empty state */}
      {vulnerabilities.length === 0 && !aiSummary && (
        <div className="col-span-full text-center py-12">
          <Shield className="w-12 h-12 mx-auto mb-4 text-muted-foreground" />
          <p className="text-muted-foreground">
            No relevant threats found for your tech stack. You're all clear!
          </p>
        </div>
      )}
    </main>
  );
}