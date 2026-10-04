# Spec: PatchPal - Security Threat Digest for a Friend

## Objective

**"Build for a Friend"** — PatchPal is a local-first web application that fetches security vulnerability feeds and trending threat news, filters them by a friend's tech stack, and uses Gemma (open-source AI) to summarize them into a beautiful, actionable daily dashboard.

**The friend:** A developer friend who uses specific technologies (e.g., Node.js, Python, React, PostgreSQL) and doesn't have time to track CVEs, zero-days, or security advisories manually. PatchPal watches their stack and surfaces only what matters to them, in a clean, minimal UI.

**Why open innovation matters:** PatchPal runs 100% locally with Gemma via Ollama. Your friend's tech stack profile never leaves their machine. No cloud API sees what they run. They can swap models, fine-tune, or audit every prompt. It costs nothing to run after setup.

## Tech Stack

**Backend (API & AI Processing):**
- **Language:** Python 3.11+
- **Framework:** FastAPI
- **AI Model:** Gemma 2 (via Ollama, local inference)
- **Feed Sources:** RSS/Atom (NVD, CISA KEV, GitHub Advisories) + SerpApi (live trending threat search)
- **Config:** YAML (friend profile)

**Frontend (Dashboard UI):**
- **Framework:** Next.js (App Router, React 19)
- **Styling:** Tailwind CSS v4 + native CSS Grid
- **Animation:** `motion/react` (Framer Motion)
- **Icons:** `@phosphor-icons/react`
- **Typography:** Geist Sans (clean, minimal B2B/consumer aesthetic per `design-taste-frontend`)
- **State:** React Hooks (SWR or React Query for fetching)

## Commands

```bash
# Backend (Python)
cd backend
pip install -e ".[dev]"
fastapi dev src/patchpal/main.py

# Frontend (Next.js)
cd frontend
npm install
npm run dev
```

## Project Structure

```
patchpal/
  SPEC.md
  LICENSE                  (MIT)
  README.md
  backend/
    pyproject.toml
    profiles/
      friend.yaml            (friend's tech stack config)
    src/patchpal/
      main.py               (FastAPI entry point)
      api/                  (routers)
      core/
        profile.py          (load/validate friend profile YAML)
        feeds.py            (RSS/Atom fetcher - NVD, CISA, GitHub)
        search.py           (SerpApi live threat search)
        summarizer.py       (Gemma via Ollama - filter + summarize)
        models.py           (dataclasses: Vulnerability, Digest, FriendProfile)
    tests/                  (pytest suite)
  frontend/
    package.json
    next.config.mjs
    tailwind.config.ts
    src/
      app/                  (Next.js pages/layout)
      components/           (UI components, Bento grid, Vulnerability cards)
      lib/                  (API client)
```

## Code Style & Design Guidelines

**Frontend (Anti-Slop `tasteskill` applied):**
- **Vibe:** Clean, minimalist, dashboard for a developer. Geist Sans, neutral gray background (`bg-zinc-50` or `bg-zinc-950`), with a single clear accent color (e.g., Electric Blue or Emerald for safe status, minimal red for critical).
- **Layout:** Bento-style CSS Grid for the dashboard. No complex flexbox math.
- **Motion:** Restrained (Motion Intensity 3-4). Subtle fade-ins for feed items.
- **Typography:** `Geist` font. Clean hierarchical sizing (e.g., `text-4xl tracking-tighter`).

**Backend (Python):**
- Snake_case for functions/variables, PascalCase for classes
- Type hints on all function signatures
- FastAPI routing with Pydantic response models
- No global state; pass dependencies explicitly

## Testing Strategy

- **Backend:** `pytest` in `backend/tests/`, mocking HTTP and Ollama calls.
- **Frontend:** ESLint + Prettier, manual visual testing.
- **Coverage:** Core logic (profile, feeds, summarizer, API routes).

## Boundaries

- **Always:** Run tests before considering a task done. Validate all external input (feed XML, API responses).
- **Ask first:** Adding new dependencies. Changing the profile YAML schema. Adding new feed sources.
- **Never:** Send friend's tech stack data to any cloud service (local-only AI). Commit API keys. Mix UI frameworks or icon libraries.

## Success Criteria

1. Backend FastAPI serves data successfully based on `profiles/friend.yaml`.
2. Next.js frontend fetches the API and displays a clean, minimal dashboard of relevant threats.
3. Digest contains only vulnerabilities relevant to the friend's tech stack.
4. Summaries are in friendly plain language (not raw CVE text), powered locally by Gemma.
5. Works fully offline once feeds are cached (except for SerpApi, which degrades gracefully).
6. Tests pass, lint clean, builds clean.
7. README explains setup and usage clearly.
8. DEV submission post written with required tags.

## Partner Categories Targeted

| Partner | How We Use It | Prize |
|---------|--------------|-------|
| **Gemma** (Featured) | Core AI - local summarization + relevance filtering | $200 |
| **SerpApi** (Partner) | Live web search for trending security threats | $100 |
| **Sentry Agent Tracing** (Partner) | Trace Gemma inference calls, show performance in write-up | $100 |

## Open Questions

- Should the frontend allow dynamic editing of the tech stack profile, or is read-only from the YAML sufficient for the MVP?
- Does the friend actually exist and can we get their reaction? (Bonus points per challenge rules)

