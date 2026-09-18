"""Application configuration via environment variables.

No defaults with secret values are ever written here; all secrets
must be provided through a local .env file (never committed).
"""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# apps/api/ — the directory containing this module; the env file lives here
# regardless of whether the backend is launched from the repo root or apps/api.
BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """Typed application settings loaded from the environment."""

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Nexus AI API"
    environment: str = "development"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    log_level: str = "info"


@lru_cache
def get_settings() -> Settings:
    """Return a cached settings instance."""
    return Settings()


settings = get_settings()