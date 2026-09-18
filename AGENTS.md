# AGENTS.md — Nexus AI

**Project:** Nexus AI — Agentic Enterprise Research & Knowledge System

This file defines the development rules and architecture principles for this repository. All contributors and AI agents MUST read and follow it before writing code.

---

## 1. Project Overview

Nexus AI is an agentic enterprise research and knowledge system. It combines LLM-driven agents with retrieval, tools, and structured data access to answer complex research questions, grounded in enterprise knowledge and verified outputs.

The repository is intentionally initialized in stages. **No application source code exists yet**; this document establishes the rules that govern all future work.

---

## 2. Planned Technology Stack (Fixed Decisions)

The following choices are settled. Do not substitute alternatives without explicit approval.

| Layer | Technology |
|---|---|
| Backend API | FastAPI + Python |
| Frontend | Next.js + TypeScript |
| Agent orchestration | LangGraph |
| Primary database | PostgreSQL |
| Vector search | pgvector (planned, on PostgreSQL) |
| Local model runtime | Ollama (optional layer only) |
| LLM inference (dev) | Cloud LLM APIs (primary) |

### Notes

- **PostgreSQL is the single primary database.** pgvector will be used for vector search within it. Do not introduce additional databases (no Supabase, no separate vector-only stores) unless a rule change is agreed first.
- **Ollama is optional.** The system must never depend on a large local LLM being available. All core functionality must work with cloud inference.
- **Cloud LLM inference is the primary development path.**

---

## 3. Architecture Principles

### 3.1 Layered Separation (mandatory)

The system maintains a clear separation between five layers. Code in one layer must not bypass boundaries into another.

```
Frontend (Next.js/TS)
        |
Backend API (FastAPI)
        |
Agent Layer (LangGraph orchestration)
        |
Tools Layer (search, calculator/Python, SQL, retrieval, ...)
        |
Database Layer (PostgreSQL + pgvector, server-side only)
```

- The **frontend never talks to the database or LLM providers directly.** All data access goes through the backend API.
- The **agent layer** decides *what* to do; the **tools layer** defines *how* it is done; the **database layer** persists results.
- Business logic lives server-side. The frontend is a presentation surface.

### 3.2 Modularity & Future Protocols

- Keep the architecture **modular so MCP (Model Context Protocol) and A2A (Agent-to-Agent) can be introduced later** without rewrites.
- Agents, tools, and model clients should be defined behind clean interfaces so providers/protocols can be swapped.
- Do not hard-wire a specific LLM vendor into agent logic; isolate model calls.

### 3.3 Planned Capabilities (design for, but do not assume early)

The system will eventually include, each as a separate module:

- RAG (retrieval-augmented generation) over enterprise knowledge
- Web search tool
- Python / calculator tool
- SQL tools (server-side execution only)
- Memory
- Verification (output checking)
- Evaluation (test harnesses for agent behavior)
- Observability (tracing, logging, metrics)

Capabilities land as independent modules; the orchestrator composes them. No capability may become a hidden dependency of the core API.

---

## 4. Security Rules (non-negotiable)

1. **Never commit secrets.** No API keys, tokens, passwords, or connection strings in code, tests, fixtures, or git history.
2. **Use environment variables** (`.env`, excluded from git; provide `.env.example` with placeholder values instead).
3. **Validate all inputs** at the API boundary before they reach agents, tools, or the database.
4. **Database access is server-side only.** Only the backend/database layer holds credentials. The frontend receives no DB credentials.
5. **SQL tools** execute only through controlled, parameterized server-side paths — never by interpolating user or LLM output into raw SQL.
6. Maintain least privilege: each component gets only the access it needs.
7. Keep dependencies explicit and pinned; review anything added.

---

## 5. Development Rules

1. **Do not create application source code yet** unless a task explicitly asks for it. Early changes are limited to documentation, scaffolding agreements, and configuration *patterns* (not secrets).
2. **Do not install packages yet** until the project scaffolding task explicitly begins.
3. **Do not add Docker configuration yet.**
4. **Do not use Supabase.** PostgreSQL is the database.
5. **Do not make architectural assumptions beyond this document.** If a decision is not recorded here, ask before implementing.
6. When implementation begins, record significant new decisions in this file so it remains the single source of truth.
7. Keep commits small and focused; write clear commit messages.

---

## 6. Repository Conventions (actual layout)

The repository is organized as follows (established in scaffolding; recorded in `docs/ADR.md`, ADR-0001):

```
apps/
  api/        # FastAPI + Python backend (API, DB access, server-side logic)
  web/        # Next.js + TypeScript frontend (UI only, no DB access)
core/         # Python packages: agent/, rag/, tools/, memory/, evaluation/
database/     # migrations/ and seeds/ (PostgreSQL + pgvector, configured later)
tests/        # test suites
docs/         # Architecture docs and decisions (docs/ADR.md)
scripts/      # development and operations scripts
```

The backend is launched from the repository root as a package (e.g., `python -m uvicorn apps.api.main:app`); environment files are application-local: `apps/api/.env` and `apps/web/.env.local` (both gitignored; only `*.env.example` templates are tracked).

---

## 7. Change Discipline

- Any change to the technology stack or architecture principles requires updating this file in the same change.
- Agents must re-read this file at the start of any session in this repository.