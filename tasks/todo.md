## Task 1: Scaffold FastAPI backend structure + dependencies

**Description:** Initialize the `backend/` directory, set up `pyproject.toml` with dependencies, configure linting/testing (ruff, pytest), and create the entry points.

**Acceptance criteria:**
- [x] `pyproject.toml` defines dependencies (fastapi, uvicorn, httpx, feedparser, ollama, pyyaml, pydantic, serpapi).
- [x] `backend/src/patchpal/` and `backend/tests/` directories exist with `__init__.py`.
- [x] `ruff` and `pytest` configuration included.
- [x] `pip install -e ".[dev]"` installs successfully.

**Verification:**
- [x] Tests pass: `pytest backend/tests/` (runs without error)
- [x] Build succeeds: `pip install -e .`

**Dependencies:** None
**Estimated scope:** Small

---

## Task 2: Implement core models (Pydantic/dataclasses)

**Description:** Define the core models for the backend API: `FriendProfile`, `Vulnerability`, and `Digest`.

**Acceptance criteria:**
- [ ] Models are defined using Pydantic (or dataclasses) for easy FastAPI integration.
- [ ] Models include necessary fields (tech_stack, cve_id, title, etc.).

**Verification:**
- [ ] Tests pass: `pytest backend/tests/test_models.py`

**Dependencies:** Task 1
**Estimated scope:** Small

---

## Task 3: Implement profile loader (YAML config)

**Description:** Implement functionality to load a friend's profile from a YAML file and validate it.

**Acceptance criteria:**
- [ ] `load_profile(filepath)` reads YAML and returns a `FriendProfile` object.
- [ ] Includes a default template profile generation function.

**Verification:**
- [ ] Tests pass: `pytest backend/tests/test_profile.py`

**Dependencies:** Task 2
**Estimated scope:** Small

---

## Task 4: Implement feeds.py + search.py

**Description:** Fetch security RSS feeds (NVD, CISA) and query SerpApi.

**Acceptance criteria:**
- [ ] `fetch_rss_feeds()` fetches and parses XML into `Vulnerability` objects.
- [ ] `search_threat_news()` queries SerpApi and degrades gracefully.

**Verification:**
- [ ] Tests pass: `pytest backend/tests/test_feeds.py` and `test_search.py`

**Dependencies:** Task 2
**Estimated scope:** Medium

---

## Task 5: Implement summarizer.py (Gemma via Ollama)

**Description:** The AI engine. Use Gemma to filter vulnerabilities and summarize them defensively.

**Acceptance criteria:**
- [ ] `filter_relevant()` and `generate_friendly_summary()` use Ollama SDK.
- [ ] System prompts are explicitly defensive.

**Verification:**
- [ ] Tests pass: `pytest backend/tests/test_summarizer.py`

**Dependencies:** Task 2
**Estimated scope:** Medium

---

## Task 6: Wire up FastAPI endpoints

**Description:** Expose the backend logic via FastAPI routes (`/api/digest`, `/api/profile`).

**Acceptance criteria:**
- [ ] `/api/digest` endpoint orchestrates feed fetching, AI summarization, and returns the digest JSON.
- [ ] CORS is configured to allow the Next.js frontend to connect.

**Verification:**
- [ ] Tests pass: `pytest backend/tests/test_api.py` (using TestClient)
- [ ] Build succeeds: `fastapi dev` runs successfully.

**Dependencies:** Tasks 1-5
**Estimated scope:** Medium

---

## Task 7: Scaffold Next.js frontend

**Description:** Create the `frontend/` directory with Next.js, Tailwind v4, and Phosphor Icons.

**Acceptance criteria:**
- [ ] `npx create-next-app@latest frontend` with App Router, TypeScript.
- [ ] Tailwind CSS v4 is configured.
- [ ] Dependencies added: `motion/react`, `@phosphor-icons/react`, `swr`.

**Verification:**
- [ ] Frontend runs: `npm run dev` in `frontend/` starts server without errors.

**Dependencies:** None
**Estimated scope:** Small

---

## Task 8: Set up global styles and typography

**Description:** Implement the minimalist, anti-slop design rules from `design-taste-frontend`.

**Acceptance criteria:**
- [ ] Geist font is configured globally.
- [ ] Neutral palette (Zinc/Slate) with one accent color (e.g., Electric Blue).
- [ ] Minimal CSS resets and basic layout wrappers added to `app/layout.tsx`.

**Verification:**
- [ ] Visual check: `localhost:3000` reflects the clean Geist typography.

**Dependencies:** Task 7
**Estimated scope:** Small

---

## Task 9: Implement data fetching hook

**Description:** Create the SWR hook to fetch the digest from the FastAPI backend.

**Acceptance criteria:**
- [ ] `useDigest()` hook connects to `http://localhost:8000/api/digest`.
- [ ] Handles loading and error states properly.

**Verification:**
- [ ] Manual check: Fetch returns the expected JSON structure.

**Dependencies:** Tasks 6, 7
**Estimated scope:** Small

---

## Task 10: Build Bento grid UI and components

**Description:** Build the dashboard UI displaying the threat cards and AI summary.

**Acceptance criteria:**
- [ ] Dashboard uses CSS Grid (Bento style).
- [ ] Vulnerability cards display title, severity, and affected tech.
- [ ] AI Summary is displayed prominently.
- [ ] Restrained motion (fade-in) using `motion/react`.

**Verification:**
- [ ] Visual check: The dashboard looks beautiful, minimalist, and responsive.

**Dependencies:** Tasks 8, 9
**Estimated scope:** Large

---

## Task 11: Write README.md

**Description:** Document the project for end users (setup instructions for frontend + backend).

**Acceptance criteria:**
- [ ] README includes setup instructions (install Ollama, Next.js, Python), usage, and "Why open innovation matters" paragraph.

**Verification:**
- [ ] Manual check: README renders well.

**Dependencies:** Tasks 1-10
**Estimated scope:** Small

---

## Task 12: Draft DEV submission post + save agent session

**Description:** Prepare the final submission for the DEV Challenge using DevRelay.

**Acceptance criteria:**
- [ ] Post includes architecture details and tags `#devchallenge, #weekendchallenge, #hf26challenge`.
- [ ] Embed the agent workflow transcript via DevRelay.

**Verification:**
- [ ] Manual check: DEV draft looks correct.

**Dependencies:** Task 11
**Estimated scope:** Medium
