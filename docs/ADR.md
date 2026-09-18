# Architecture Decision Records

Significant technical decisions for Nexus AI are recorded here as short entries. The authoritative rules remain in the root `AGENTS.md`.

## ADR-0001 — Repository scaffolding layout

- **Date:** 2026-09-18
- **Status:** Accepted
- **Decision:** Adopt a monorepo layout with `apps/api` (FastAPI backend), `apps/web` (Next.js frontend), `core/` (agent, rag, tools, memory, evaluation packages), `database/` (migrations, seeds), `tests/`, `docs/`, `scripts/`.
- **Consequences:** Replaces the indicative `backend/ frontend/ agents/ tools/` layout in AGENTS.md §6; core agent/tool logic lives in `core/` as Python packages consumed by the API.