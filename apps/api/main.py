"""Nexus AI API — FastAPI application entry point.

Scaffolding only: no database, auth, agent, or RAG yet.
"""

from fastapi import FastAPI

from apps.api.config import settings

app = FastAPI(
    title="Nexus AI API",
    description="Agentic Enterprise Research & Knowledge System",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health() -> dict:
    """Liveness probe for the API service."""
    return {"status": "ok", "service": "nexus-ai-api", "version": app.version}


@app.get("/", tags=["system"])
def root() -> dict:
    """Basic service metadata."""
    return {
        "name": settings.app_name,
        "environment": settings.environment,
        "docs": "/docs",
    }