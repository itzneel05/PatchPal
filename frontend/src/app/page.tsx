"use client";

import { useDigest } from "@/hooks/use-digest";
import { ShieldCheck, MagnifyingGlass } from "@phosphor-icons/react";
import { useMemo, useState } from "react";

function SeverityDot({ severity }: { severity: string }) {
  const map: Record<string, string> = {
    Critical: "bg-red-500",
    High: "bg-orange-500",
    Medium: "bg-amber-500",
    Low: "bg-zinc-400",
  };
  return <span className={`inline-block size-2 rounded-full ${map[severity] ?? map.Low}`} aria-label={severity} />;
}

function stripHtml(raw: string) {
  return raw.replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();
}

export default function Home() {
  const { data: digest, isLoading, isError, error, mutate } = useDigest();
  const [query, setQuery] = useState("");
  const [severityFilter, setSeverityFilter] = useState<"all" | "critical" | "high" | "medium" | "low">("all");

  const filtered = useMemo(() => {
    return (digest?.vulnerabilities ?? []).filter((t) => {
      const matchesQuery =
        !query ||
        t.title.toLowerCase().includes(query.toLowerCase()) ||
        (t.affected_tech ?? []).some((tech) => tech.toLowerCase().includes(query.toLowerCase()));
      const matchesSeverity = severityFilter === "all" || t.severity.toLowerCase() === severityFilter;
      return matchesQuery && matchesSeverity;
    });
  }, [digest, query, severityFilter]);

  if (isLoading && !digest) {
    return (
      <main className="flex min-h-screen items-center justify-center bg-[#f7f5f2]">
        <p className="text-base text-zinc-500">Loading your digest...</p>
      </main>
    );
  }

  if (isError) {
    return (
      <main className="flex min-h-screen flex-col items-center justify-center gap-4 bg-[#f7f5f2] p-8 text-center">
        <p className="text-lg font-medium text-red-600">Something went wrong</p>
        <p className="max-w-lg text-base text-zinc-600">{error?.message ?? "Unable to load the digest."}</p>
        <button onClick={() => mutate()} className="rounded-md bg-[#1f1f1f] px-4 py-2 text-sm font-medium text-white hover:bg-[#333333]">
          Retry
        </button>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-[#f7f5f2] text-[#1f1f1f]">
      <div className="mx-auto max-w-4xl space-y-16 p-6 md:p-16">
        <header className="space-y-3">
          <h1 className="text-5xl font-bold tracking-tight">{digest?.friend_name ?? "Friend"} Digest</h1>
          <p className="text-xl text-zinc-600">{digest?.date_generated ?? "Today"}</p>
        </header>

        <div className="flex items-center justify-between gap-4">
          <div className="flex items-center gap-3 rounded-full border border-[#e5e0da] bg-white px-5 py-4">
            <MagnifyingGlass className="size-5 text-zinc-400" />
            <input
              type="text"
              placeholder="Search threats or tech..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="w-56 bg-transparent text-lg outline-none placeholder:text-zinc-400"
            />
          </div>
          <button
            onClick={() => mutate()}
            className="rounded-full bg-[#1f1f1f] px-6 py-3 text-base font-medium text-white hover:bg-[#333333]"
          >
            Refresh
          </button>
        </div>

        {digest?.ai_summary ? (
          <section className="border-l-4 border-[#c97d4b] bg-white p-8">
            <h2 className="mb-4 text-2xl font-semibold">AI Advisory</h2>
            <p className="text-lg leading-relaxed text-zinc-700">{digest.ai_summary}</p>
          </section>
        ) : null}

        <div className="flex gap-3">
          {(["all", "critical", "high", "medium", "low"] as const).map((s) => (
            <button
              key={s}
              onClick={() => setSeverityFilter(s)}
              className={`rounded-full px-5 py-2 text-base font-medium capitalize ${
                severityFilter === s
                  ? "bg-[#c97d4b] text-white"
                  : "border border-[#e5e0da] bg-white text-zinc-600 hover:bg-[#e5e0da]"
              }`}
            >
              {s}
            </button>
          ))}
        </div>

        <section className="space-y-10">
          <h2 className="text-3xl font-semibold">Vulnerabilities</h2>
          {filtered.length > 0 ? (
            <div className="divide-y divide-[#e5e0da]">
              {filtered.map((t, idx) => (
                <article key={t.cve_id ?? idx} className="py-8">
                  <div className="mb-3 flex items-center gap-3">
                    <SeverityDot severity={t.severity} />
                    <h3 className="text-xl font-semibold leading-snug">{t.title}</h3>
                  </div>
                  <p className="text-sm text-zinc-500">{t.severity} · {t.affected_tech?.join(", ") ?? "Unknown"}</p>
                  <p className="mt-3 text-lg leading-relaxed text-zinc-700">{stripHtml(t.raw_description)}</p>
                  <a href={t.source_url} target="_blank" rel="noreferrer" className="mt-4 inline-block text-base font-medium text-[#c97d4b] hover:underline">
                    View source
                  </a>
                </article>
              ))}
            </div>
          ) : (
            <div className="flex flex-col items-center justify-center rounded-3xl border border-dashed border-[#e5e0da] p-16 text-center">
              <ShieldCheck className="mb-6 size-16 text-zinc-400" />
              <p className="text-lg text-zinc-500">No matching threats. Adjust filters or refresh.</p>
            </div>
          )}
        </section>
      </div>
    </main>
  );
}
