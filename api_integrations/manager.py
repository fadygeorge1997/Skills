"""
API Manager - Centralized access to all API clients.

Provides unified interface for managing multiple AI service integrations.
"""

import logging
from typing import Dict, List, Optional, Type

from .composio_client import ComposioClient
from .config import Settings, get_settings
from .errors import ConfigurationError, IntegrationError
from .gemini_client import GeminiClient, get_gemini_client
from .langsmith_client import LangSmithClient, get_langsmith_client
from .minimax_client import MinimaxClient, get_minimax_client
from .secrets import SecretsManager, get_secrets_manager

logger = logging.getLogger(__name__)


class APIManager:
    """
    Centralized manager for all API integrations.

    Provides:
    - Unified access to all API clients
    - Health monitoring
    - Configuration management
    - Error handling
    - Usage tracking

    Example:
        manager = APIManager()

        # Access individual clients
        gemini_response = manager.gemini.generate_text("Hello")
        minimax_response = manager.minimax.generate_text("你好")

        # Health check all services
        health = manager.health_check_all()

        # Get usage report
        report = manager.get_usage_report()
    """

    def __init__(self, settings: Optional[Settings] = None):
        """
        Initialize API manager.

        Args:
            settings: Optional settings instance (loads from env if not provided)
        """
        self.settings = settings or get_settings()
        self.secrets = get_secrets_manager()

        # Initialize clients (lazy loading)
        self._composio: Optional[ComposioClient] = None
        self._langsmith: Optional[LangSmithClient] = None
        self._minimax: Optional[MinimaxClient] = None
        self._gemini: Optional[GeminiClient] = None

        self._health_status: Dict[str, bool] = {}

        logger.info("APIManager initialized")

    @property
    def composio(self) -> ComposioClient:
        """Get Composio client (initializes on first access)."""
        if self._composio is None:
            self._composio = ComposioClient()
        return self._composio

    @property
    def langsmith(self) -> LangSmithClient:
        """Get LangSmith client (initializes on first access)."""
        if self._langsmith is None:
            self._langsmith = LangSmithClient()
        return self._langsmith

    @property
    def minimax(self) -> MinimaxClient:
        """Get Minimax client (initializes on first access)."""
        if self._minimax is None:
            self._minimax = MinimaxClient()
        return self._minimax

    @property
    def gemini(self) -> GeminiClient:
        """Get Gemini client (initializes on first access)."""
        if self._gemini is None:
            self._gemini = get_gemini_client()
        return self._gemini

    def health_check_all(self) -> Dict[str, bool]:
        """
        Check health of all API integrations.

        Returns:
            Dictionary mapping service names to health status
        """
        health_status = {}

        logger.info("Running health checks for all services...")

        services = [
            ("composio", lambda: self.composio.health_check()),
            ("langsmith", lambda: self.langsmith.health_check()),
            ("minimax", lambda: self.minimax.health_check()),
            ("gemini", lambda: self.gemini.health_check()),
        ]

        for name, check_func in services:
            try:
                health_status[name] = check_func()
                status = "✓ Healthy" if health_status[name] else "✗ Unhealthy"
                logger.info(f"  {name}: {status}")
            except Exception as e:
                health_status[name] = False
                logger.error(f"  {name}: ✗ Error - {e}")

        self._health_status = health_status
        return health_status

    def get_usage_report(self) -> Dict[str, any]:
        """
        Get comprehensive usage report for all services.

        Returns:
            Usage report dictionary
        """
        report = {
            "services": {},
            "secrets": self.secrets.get_usage_report(),
            "health": self._health_status,
        }

        # Add service-specific info
        for name in ["composio", "langsmith", "minimax", "gemini"]:
            report["services"][name] = {
                "configured": True,
                "api_key_masked": self.secrets.mask_secret(name),
            }

        return report

    def generate_text(
        self,
        prompt: str,
        provider: str = "auto",
        **kwargs
    ) -> str:
        """
        Generate text using the specified provider.

        Args:
            prompt: Text prompt
            provider: Provider to use ('gemini', 'minimax', or 'auto')
            **kwargs: Additional parameters

        Returns:
            Generated text
        """
        if provider == "auto":
            # Try providers in order of preference
            providers = ["gemini", "minimax"]
            for prov in providers:
                if self._health_status.get(prov, False):
                    provider = prov
                    break
            else:
                provider = "gemini"  # Default fallback

        if provider == "gemini":
            return self.gemini.generate_text(prompt, **kwargs)
        elif provider == "minimax":
            return self.minimax.generate_text(prompt, **kwargs)
        else:
            raise ValueError(f"Unknown provider: {provider}")

    def close(self) -> None:
        """Clean up resources."""
        logger.info("Closing API manager connections")
        self._composio = None
        self._langsmith = None
        self._minimax = None
        self._gemini = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class APIRegistry:
    """
    Registry for managing multiple API configurations.

    Useful for multi-tenant or multi-environment setups.
    """

    def __init__(self):
        self._managers: Dict[str, APIManager] = {}

    def register(self, name: str, manager: APIManager) -> None:
        """Register an API manager."""
        self._managers[name] = manager

    def get(self, name: str) -> APIManager:
        """Get a registered manager."""
        if name not in self._managers:
            raise KeyError(f"No manager registered with name: {name}")
        return self._managers[name]

    def health_check_all(self) -> Dict[str, Dict[str, bool]]:
        """Check health of all registered managers."""
        return {
            name: manager.health_check_all()
            for name, manager in self._managers.items()
        }


# Singleton instance
_manager: Optional[APIManager] = None


def get_api_manager() -> APIManager:
    """Get or create the global API manager instance."""
    global _manager
    if _manager is None:
        _manager = APIManager()
    return _manager
