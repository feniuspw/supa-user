from functools import lru_cache
import logging
import os

try:
    from pydantic import BaseSettings
except Exception:  # pragma: no cover - fallback for environments without pydantic-settings
    logging.getLogger(__name__).warning(
        "pydantic BaseSettings unavailable, using fallback settings loader"
    )

    from pydantic import BaseModel

    class BaseSettings(BaseModel):
        def __init__(self, **data):
            for field in self.model_fields:
                data.setdefault(field, os.environ.get(field))
            super().__init__(**data)


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    SUPABASE_URL: str
    SUPABASE_API_KEY: str
    SSO_REDIRECT_TO: str = "http://localhost"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> "Settings":
    settings = Settings()
    logging.getLogger(__name__).debug("Settings loaded: %s", settings.dict())
    return settings

