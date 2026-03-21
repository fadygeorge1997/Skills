"""
Configuration module using Pydantic Settings.
Loads and validates environment variables.
"""

from functools import lru_cache
from typing import Optional

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    All API keys are validated and securely stored.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Composio Configuration
    composio_api_key: str = Field(
        ...,
        description="Composio API Key",
        alias="COMPOSIO_API_KEY",
    )

    # LangSmith Configuration
    langsmith_api_key: str = Field(
        ...,
        description="LangSmith API Key",
        alias="LANGSMITH_API_KEY",
    )
    langsmith_endpoint: str = Field(
        default="https://api.smith.langchain.com",
        description="LangSmith API Endpoint",
        alias="LANGSMITH_ENDPOINT",
    )
    langsmith_project: str = Field(
        default="default",
        description="LangSmith Project Name",
        alias="LANGSMITH_PROJECT",
    )
    langsmith_tracing: bool = Field(
        default=True,
        description="Enable LangSmith Tracing",
        alias="LANGSMITH_TRACING",
    )

    # Minimax Configuration
    minimax_api_key: str = Field(
        ...,
        description="Minimax API Key",
        alias="MINIMAX_API_KEY",
    )
    minimax_base_url: str = Field(
        default="https://api.minimaxi.chat",
        description="Minimax API Base URL",
        alias="MINIMAX_BASE_URL",
    )

    # Gemini Configuration
    gemini_api_key: str = Field(
        ...,
        description="Google Gemini API Key",
        alias="GEMINI_API_KEY",
    )
    gemini_model: str = Field(
        default="gemini-2.0-flash",
        description="Gemini Model Name",
        alias="GEMINI_MODEL",
    )

    @field_validator(
        "composio_api_key",
        "langsmith_api_key",
        "minimax_api_key",
        "gemini_api_key",
    )
    @classmethod
    def validate_api_key(cls, v: str, info) -> str:
        """Validate that API keys are not placeholders."""
        field_name = info.field_name
        placeholder_patterns = [
            "your-",
            "placeholder",
            "xxx",
            "changeme",
            "sk-test",
        ]

        if any(pattern in v.lower() for pattern in placeholder_patterns):
            raise ValueError(
                f"{field_name} appears to be a placeholder value: {v[:20]}..."
                f"\nPlease set a valid API key in your .env file"
            )

        # Check key format based on provider
        if field_name == "gemini_api_key" and not v.startswith("AIza"):
            raise ValueError(
                f"Invalid Gemini API key format. Expected to start with 'AIza'"
            )

        if field_name == "langsmith_api_key" and not v.startswith("lsv2_"):
            raise ValueError(
                f"Invalid LangSmith API key format. Expected to start with 'lsv2_'"
            )

        return v

    def get_masked_key(self, key_name: str) -> str:
        """Return a masked version of an API key for logging."""
        key = getattr(self, key_name, "")
        if len(key) > 8:
            return f"{key[:4]}...{key[-4:]}"
        return "****"


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.
    Uses LRU cache to avoid reloading .env file on every call.
    """
    return Settings()


# Export for convenience
settings = get_settings()
