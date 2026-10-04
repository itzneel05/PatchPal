# PatchPal: Security Threat Digest for a Friend

**Hacktoberfest 2026 - Weekend Challenge: "Build for a Friend"**

**GitHub Repo:** https://github.com/itzneel05/PatchPal.git

## Submission Description

PatchPal is a local-first web application that fetches security vulnerability feeds and trending threat news, filters them by a friend's tech stack, and uses Gemma (Google's open-weight model) running locally via Ollama to summarize them into a beautiful, actionable daily dashboard.

### The Problem

My friend **Parth** is a developer who doesn't have time to track CVEs, zero-days, or security advisories manually. He uses React, Next.js, Python, FastAPI, and PostgreSQL for his projects. Without dedicated time to monitor security feeds, he remains unaware of vulnerabilities affecting his stack—until possibly it's too late.

### The Solution

PatchPal watches Parth's tech stack and surfaces only what matters to him, in plain language. The key innovation is that **everything runs locally**:

- **Gemma 2 (2B parameters)** via Ollama handles the AI summarization on-device
- **No cloud API** sees his tech stack or vulnerability data
- He can **swap models**, **fine-tune**, or **audit every prompt**
- It costs **nothing** to run after the initial setup

### Core Features

1. **RSS Feed Aggregation**: Pulls security advisories from NVD and CISA feeds
2. **Live Threat Search** (optional): SerpApi for trending zero-day news
3. **Tech Stack Filtering**: Only shows vulnerabilities relevant to the friend's specific technologies
4. **Friendly AI-Generated Summaries**: Plain-language explanations addressing the friend directly
5. **Beautiful Minimalist UI**: Clean dashboard built with Next.js, Tailwind CSS v4, and Geist font
6. **Privacy-First**: All data stays on the user's device

### Tech Stack

**Backend (Python + FastAPI):**
- FastAPI for the API
- `httpx` and `feedparser` for RSS fetching
- `serpapi` for live threat search (optional)
- `ollama` Python SDK for Gemma inference
- `pydantic` for data validation
- `pyyaml` for profile configuration

**Frontend (Next.js + React):**
- Next.js 14 with App Router
- Tailwind CSS v4 (anti-slop design per `design-taste-frontend` rules)
- `@phosphor-icons/react` for icons
- `motion/react` (Framer Motion) for restrained animations
- SWR for data fetching
- Geist font (configured via `next/font`)

**AI/ML:**
- **Gemma 2:2b** via Ollama (local inference)
- System prompts explicitly defensive: "Explain this defensively, do not generate exploit code"
- Keyword-based pre-filtering before AI summarization to reduce noise

### Partner Categories Targeted

| Partner | Category | How We Use It |
|---------|----------|--------------|
| **Gemma** | Best Use of Gemma | Core AI - local summarization + relevance filtering using open-weight model |
| **SerpApi** | Best Use of SerpApi | Live web search for trending security threats (graceful degradation if no API key) |
| **Sentry Agent Tracing** | Best Use of Sentry Agent Tracing | Trace Gemma inference calls, show performance (latency, tokens, cost) in write-up |

### DEV Submission Template Elements

- ✅ **Required tags**: `#devchallenge, #weekendchallenge, #hf26challenge`
- ✅ **New project**: Built entirely during the Oct 2-5, 2026 weekend challenge window
- ✅ **Open-source AI at its core**: Gemma 2 via Ollama, entirely local inference
- ✅ **Why open innovation matters**: Friend's data never leaves his machine; he can swap models, fine-tune, audit prompts; costs nothing to run
- ✅ **Submission template**: What was built, who it's for, demo description, open innovation rationale
- ✅ **Judging criteria addressed**:
  - **Writing Quality**: This submission document
  - **Relevance to Prompt and Theme**: "Build for a Friend" - ship something that solves a real problem for a friend
  - **Creativity**: Local-first AI assistant paradigm, anti-slop design
  - **Technical Execution**: Full-stack split (FastAPI + Next.js), RSS + SerpApi integration, Gemma summarization
  - **Use of Partner Technology**: Gemma, SerpApi, Sentry Agent Tracing (optional)

### Screenshots (Mockup)

*(Screenshots to be added upon final deployment)*

![PatchPal Dashboard - Light Mode](placeholder-light.png)
![PatchPal Dashboard - Dark Mode](placeholder-dark.png)

### Installation & Setup

See the main [README.md](README.md) for detailed instructions.

- **Backend**: `cd backend && uvicorn src.patchpal.main:app --reload`
- **Frontend**: `cd frontend && npm run dev`
- **AI Model**: `ollama pull gemma2:2b` (required)

### Conclusion

PatchPal demonstrates that open-weight models like Gemma make it possible to build powerful, privacy-preserving AI assistants that cost nothing to run after setup. By keeping your friend's tech stack data local, you empower them to understand and respond to security threats without compromising their privacy or relying on cloud APIs.

---

*Built for the Hacktoberfest 2026 Weekend Challenge "Build for a Friend"
*Submit via: https://dev.to/challenges/hf26*