"use client";

import { useProfile } from "@/hooks/use-profile";
import { User } from "@phosphor-icons/react";

export default function ProfilePage() {
  const { data, error, isLoading } = useProfile();

  if (isLoading) return <p className="p-8 text-zinc-500 dark:text-zinc-400">Loading profile...</p>;
  if (error || !data) return <p className="p-8 text-red-500">Failed to load profile</p>;

  return (
    <main className="min-h-screen bg-[#f7f5f2] p-6 dark:bg-[#f7f5f2] md:p-12">
      <div className="mx-auto max-w-4xl space-y-8">
        <h1 className="text-3xl font-bold tracking-tight text-[#1f1f1f]">Friend Profile</h1>
        <div className="rounded-2xl border border-[#e5e0da] bg-white p-6">
          <div className="mb-4 flex items-center gap-3">
            <User className="size-6 text-[#c97d4b]" />
            <h2 className="text-2xl font-semibold text-[#1f1f1f]">{data.name}</h2>
          </div>
          <p className="text-base text-zinc-600">Tech Stack:</p>
          <ul className="mt-3 flex flex-wrap gap-2">
            {data.tech_stack?.map((tech) => (
              <li key={tech} className="rounded-full bg-[#f7f5f2] px-4 py-1.5 text-sm font-medium text-zinc-700">
                {tech}
              </li>
            ))}
          </ul>
          <p className="mt-5 text-base text-zinc-600">
            Minimum severity: <span className="font-semibold capitalize text-[#1f1f1f]">{data.severity_threshold}</span>
          </p>
        </div>
      </div>
    </main>
  );
}
