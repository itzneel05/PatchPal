*This is a submission for the [Hacktoberfest Weekend Challenge: Build for a Friend](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01)*

## What I Built
PatchPal is a local-first security digest built for my friend Parth. It fetches security vulnerability feeds and trending threat news, filters them by Parth's tech stack (React, Next.js, Python, FastAPI, PostgreSQL), and uses Gemma 2:2b running locally via Ollama to summarize them into a friendly, actionable daily dashboard. It solves the problem that Parth doesn't have time to manually track CVEs or security advisories.

## Demo
Local demo only: start the FastAPI backend and Next.js frontend, then visit `http://localhost:3000`.

## Code
GitHub repo: https://github.com/itzneel05/PatchPal.git

## How I Built It
I used a FastAPI Python backend to pull RSS feeds, optionally fetch live threat news via SerpApi, filter by the friend's tech stack, and send the relevant items to Gemma 2:2b through Ollama with defensive prompts. The frontend is Next.js App Router with Tailwind CSS v4, @phosphor-icons/react, and SWR for data fetching. The UI shows a digest with AI summary, severity filter, search, and source links.

## Why Does Open Innovation Matter?
Because PatchPal runs 100% locally with an open-weight model, Parth's tech stack data never leaves his machine. A closed API would require sharing that data and paying per call. Open innovation lets him audit every prompt, swap models, or fine-tune without rebuilding the product.

## My Agent Session
Saved via DevRelay (agent_session tag) - optional.

## Prize Categories
- Best Use of Gemma (primary)
- Best Use of SerpApi (optional integration)
- Best Use of Sentry Agent Tracing (documented for future tracing)
