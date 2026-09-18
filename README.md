# Nexus AI — Agentic Enterprise Research & Knowledge System

Nexus AI combines LLM-driven agents with retrieval, tools, and structured data access to answer complex research questions grounded in enterprise knowledge. Development rules and architecture principles live in [AGENTS.md](AGENTS.md) — the single source of truth.

## Current Architecture

```
Frontend (Next.js/TS)  ->  Backend API (FastAPI)  ->  Agent Layer (LangGraph, planned)
                          -> Tools Layer (planned)  ->  Database Layer (PostgreSQL + pgvector, planned)
```

- The frontend never talks to the database or LLM providers directly; all data access goes through the backend API.
- The agent layer decides *what* to do; the tools layer defines *how*; the database layer persists results.
- PostgreSQL is the single primary database (pgvector for vector search). No Supabase.
- Ollama is an optional runtime layer — the system must never depend on a large local LLM. Cloud LLM inference is the primary development path.
- The architecture stays modular so MCP (Model Context Protocol) and A2A (Agent-to-Agent) can be introduced later.

## Implementation Status

| Area | Status |
|---|---|
| Repository scaffolding (directories, packages, config patterns) | ✅ Done |
| FastAPI entry point + env-based settings | ✅ Minimal skeleton |
| Next.js + TypeScript starter structure | ✅ Minimal starter |
| PostgreSQL / pgvector connection | ⬜ Not started (directories only) |
| Agent orchestration (LangGraph) | ⬜ Not started |
| RAG | ⬜ Not started |
| Tools (search, calculator, SQL, retrieval) | ⬜ Not started |
| Memory | ⬜ Not started |
| Evaluation / verification | ⬜ Not started |
| Observability | ⬜ Not started |
| Authentication | ⬜ Not started |
| Docker configuration | ⬜ Not started (intentionally deferred) |

## Repository Layout

```
apps/api/     FastAPI backend (entry point, env-based settings)
apps/web/     Next.js + TypeScript frontend (starter only)
core/         agent/ rag/ tools/ memory/ evaluation/  (package skeletons)
database/     migrations/ seeds/  (directories only)
tests/        (empty)
docs/         (empty)
scripts/      (empty)
```

## Planned Major Capabilities

- RAG over enterprise knowledge
- Web search tool
- Python / calculator tool
- SQL tools (server-side, parameterized execution only)
- Memory
- Verification (output checking)
- Evaluation (test harnesses for agent behavior)
- Observability (tracing, logging, metrics)

Each capability lands as an independent module; the orchestrator composes them. See [AGENTS.md](AGENTS.md) for security rules and development discipline.

## Environment & Setup

Environment files are application-local and never committed:

| App | Real file (gitignored) | Template (tracked) |
|---|---|---|
| Backend (`apps/api`) | `apps/api/.env` | `apps/api/.env.example` |
| Frontend (`apps/web`) | `apps/web/.env.local` | `apps/web/.env.example` |

Copy each template to its real file and fill in values. Placeholders only — no real keys or secrets anywhere in the repository.

The backend is launched from the repository root as a package:

```
python -m uvicorn apps.api.main:app --reload
```

This requires dependencies from `apps/api/requirements.txt` to be installed in the active environment (not installed yet at the scaffolding stage).