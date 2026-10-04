# Implementation Plan: PatchPal

## Overview

PatchPal is a local-first web app that fetches security vulnerability feeds, filters by a friend's tech stack, and uses Gemma (local, open-source AI via Ollama) to generate a friendly daily dashboard. Built for the Hacktoberfest Weekend Challenge "Build for a Friend" — due Oct 5, 12:29 PM IST.

## Architecture Decisions

- **Full-Stack Split**: 
  - **Backend**: Python (FastAPI) for data gathering and AI processing. Fast, simple, robust ecosystem for RSS/HTTP/AI (`httpx`, `feedparser`, `ollama` SDK).
  - **Frontend**: Next.js + React. Guided by `design-taste-frontend` rules: clean minimalist design, Geist font, Lucide/Phosphor icons, Bento grid layout, no generic "AI purple slop".
- **Local-first AI**: Ollama + Gemma 2 (2B or 9B). No cloud AI. Friend's data stays local. This is the "open innovation matters" narrative.
- **YAML profiles**: Simple, human-editable config for each friend's tech stack. No database needed.
- **Graceful degradation**: SerpApi is optional. If no API key, skip live search and use RSS-only. If Ollama is down, output raw filtered CVEs without AI summary.

## Tool & Skill Mapping (When to Use What)

### Agent Skills (from C:\Projects\skills\agent-skills & _shared-skills)

| Phase | Skill | When |
|-------|-------|------|
| DEFINE | `spec-driven-development` | Already done (SPEC.md written) |
| DESIGN | `design-taste-frontend` | Applying minimalist dashboard design to Next.js UI |
| PLAN | `planning-and-task-breakdown` | This document |
| BUILD | `incremental-implementation` | Each task: implement one slice, test, verify, commit |
| BUILD | `test-driven-development` | RED-GREEN-REFACTOR for every module |
| VERIFY | `security-and-hardening` | Before shipping: validate input handling, no secrets, SSRF checks on feed URLs |
| SHIP | `shipping-and-launch` | Final pre-submission checklist |

### DevRelay MCP Tools

| Tool | When | Purpose |
|------|------|---------|
| `get_challenge_details` | Before submission | Verify required tags and template |
| `create_article` | Phase 5 | Draft DEV submission post (published: false) |
| `save_session` | Phase 5 | Save agent session transcript, embed in post |

## Dependency Graph

```
Backend (FastAPI)
    │
    ├── models.py (dataclasses / Pydantic)
    │       │
    │       ├── profile.py (load YAML → FriendProfile)
    │       │       │
    │       │       ├── feeds.py (fetch RSS → list[Vulnerability])
    │       │       │       │
    │       │       │       └── search.py (SerpApi → list[Vulnerability])
    │       │       │               │
    │       │       │               └── summarizer.py (Gemma: filter + summarize)
    │       │       │                       │
    │       │       │                       └── api/routes (FastAPI endpoints)
    │       │       │                               │
    │       │       │                               └── main.py (entry)
    │       │       │
Frontend (Next.js)  │
    │               │
    └── app/page.tsx (Fetches from FastAPI, displays Dashboard)
            │
            └── components/ (Bento grid, threat cards)
```

## Task List

### Phase 1: Backend Foundation (Tasks 1-3)

- [ ] Task 1: Scaffold FastAPI backend structure + dependencies
- [ ] Task 2: Implement core models (Pydantic/dataclasses)
- [ ] Task 3: Implement profile loader (YAML config)

### Checkpoint: Backend Foundation
- [ ] `pytest backend/tests/` passes
- [ ] Profile loading works with sample YAML

### Phase 2: Data & AI Layer (Tasks 4-6)

- [ ] Task 4: Implement feeds.py (RSS/Atom fetcher) + search.py (SerpApi)
- [ ] Task 5: Implement summarizer.py (Gemma via Ollama)
- [ ] Task 6: Wire up FastAPI endpoints (`/api/digest`, `/api/profile`)

### Checkpoint: Data & AI Layer
- [ ] Feed fetching and SerpApi work (or degrade gracefully)
- [ ] Summarizer produces friendly plain-language output via Ollama
- [ ] FastAPI serves JSON digest correctly

### Phase 3: Frontend Scaffolding (Tasks 7-8)

- [ ] Task 7: Scaffold Next.js frontend (Tailwind v4, Phosphor Icons)
- [ ] Task 8: Set up clean typography and global styles (Geist font, neutral palette)

### Checkpoint: Frontend Scaffolding
- [ ] Next.js app runs without errors on `localhost:3000`
- [ ] Basic styles match `design-taste-frontend` rules

### Phase 4: Dashboard UI (Tasks 9-10)

- [ ] Task 9: Implement data fetching hook to connect to FastAPI
- [ ] Task 10: Build Bento grid UI, Vulnerability cards, and AI summary view

### Checkpoint: Complete
- [ ] Frontend displays the API data beautifully
- [ ] All tests pass, lint clean
- [ ] Ready for deployment/shipping

### Phase 5: Documentation & Ship (Tasks 11-12)

- [ ] Task 11: Write README.md (setup instructions for frontend + backend)
- [ ] Task 12: Draft DEV submission post + save agent session

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Ollama/Gemma not installed on machine | High | Detect at startup, print setup instructions. Tests mock Ollama calls. |
| SerpApi rate limit or no API key | Medium | Graceful degradation: RSS-only mode. Tests use mocked responses. |
| Time pressure (due Oct 5 12:29 PM IST) | High | Vertical slices. Backend first, basic JSON. Frontend second. |

## Execution Order Summary

```
1. Backend: Scaffold → models → profile          [Foundation, test each]
2. Backend: feeds → search → summarizer → API    [Data+AI, test each with mocks]
3. Frontend: Scaffold → Styles → UI Components   [Next.js UI]
4. Ship: README → DEV post                       [Launch]
```
