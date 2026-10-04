# PatchPal - Security Threat Digest for a Friend

**Hacktoberfest 2026 - Weekend Challenge: "Build for a Friend"**

PatchPal is a local-first web application that fetches security vulnerability feeds and trending threat news, filters them by a friend's tech stack, and uses Gemma (open-source AI via Ollama) to summarize them into a beautiful, actionable daily dashboard.

## Why Open Innovation Matters

PatchPal runs **100% locally** with Gemma via Ollama. Your friend's tech stack profile never leaves their machine. No cloud API sees what they run. They can swap models, fine-tune, or audit every prompt. It costs nothing to run after setup.

## Features

- **Local AI Summarization**: Uses Gemma 2 (2B parameters) via Ollama - no cloud API keys required for the AI part
- **RSS Feed Aggregation**: Fetches security advisories from NVD/CISA feeds
- **Live Threat Search**: Optional SerpApi integration for trending zero-day news
- **Tech Stack Filtering**: Only shows vulnerabilities relevant to your friend's specific technologies
- **Friendly AI-Generated Summaries**: Plain-language explanations addressing your friend directly
- **Beautiful Minimalist UI**: Clean dashboard built with Next.js, Tailwind CSS v4, and Geist font
- **Privacy-First**: All data stays on the user's device

## Prerequisites

### Backend (Python + FastAPI)

1. [Install Ollama](https://ollama.com/download) (for Windows: run the `.exe` installer)
2. Pull the AI model:
   ```bash
   ollama pull gemma2:2b
   ```
3. Install dependencies:
   ```bash
   cd backend
   pip install -e ".[dev]"
   ```

### Frontend (Next.js)

1. Install Node.js dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. (Optional) Set up SerpApi key for live threat search:
   - Get an API key from [SerpApi](https://serpapi.com/)
   - Add it to your `.env` file: `SERPAPI_API_KEY=your_key_here`

## Running the Application

### Start the Backend

```bash
cd backend
uvicorn src.patchpal.main:app --reload
```

The API will be available at `http://localhost:8000`

### Start the Frontend

```bash
cd frontend
npm run dev
```

The dashboard will be available at `http://localhost:3000`

## Default Profile

A sample friend profile is included at `backend/profiles/friend.yaml`:

```yaml
name: Parth
tech_stack:
  - React
  - Next.js
  - Python
  - FastAPI
  - PostgreSQL
severity_threshold: medium
```

To use a different profile, create a YAML file matching the structure and update the path in `backend/src/patchpal/api/routes.py` or set the `DEFAULT_PROFILE_PATH` environment variable.

## Project Structure

```
patchpal/
├── README.md                    (this file)
├── SPEC.md                      (project specification)
├── backend/                     (FastAPI backend)
│   ├── pyproject.toml
│   ├── src/patchpal/
│   │   ├── main.py             (FastAPI entry point)
│   │   ├── api/                (routes)
│   │   ├── core/               (models, profile, feeds, search, summarizer)
│   │   └── tests/              (pytest suite)
│   └── profiles/
│       ├── friend.yaml          (default friend profile)
│       └── example.yaml         (template)
├── frontend/                    (Next.js frontend)
│   ├── package.json
│   ├── tailwind.config.ts
│   ├── src/
│   │   ├── app/                (pages and layout)
│   │   ├── components/         (UI components)
│   │   ├── hooks/              (use-digest hook)
│   │   └── lib/                (utility functions)
│   └── public/
└── tasks/                       (implementation plan)
    ├── plan.md                 (high-level plan)
    └── todo.md                 (task breakdown)
```

## Available Scripts

### Backend

```bash
cd backend
pip install -e ".[dev]"]  # Install dependencies
pytest                      # Run tests
fastapi dev src/patchpal/main.py  # Run dev server
```

### Frontend

```bash
cd frontend
npm run dev     # Start development server
npm run build   # Build for production
npm run lint    # Run ESLint
```

## Partner Categories (Hacktoberfest)

| Partner | How We Use It | Prize |
|---------|--------------|-------|
| **Gemma** (Featured) | Core AI - local summarization + relevance filtering | $200 |
| **SerpApi** (Partner) | Live web search for trending security threats | $100 |
| **Sentry Agent Tracing** (Partner) | Trace Gemma inference calls, show performance in write-up | $100 |

## Learn More

- [Hacktoberfest 2026](https://hacktoberfest.com/)
- [DEV Challenge Hub](https://dev.to/challenges/hf26)
- [Gemma 2 Documentation](https://github.com/google/gemma)
- [Ollama Documentation](https://ollama.ai/docs)
- [Next.js Documentation](https://nextjs.org/docs)
- [Tailwind CSS v4 Documentation](https://tailwindcss.com)