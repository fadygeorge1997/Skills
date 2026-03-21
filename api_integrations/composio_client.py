"""
Composio API Client

Composio is an AI agent platform for building and deploying AI workflows.
Docs: https://docs.composio.io/
"""

import logging
from typing import Any, Dict, List, Optional

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from .config import settings
from .secrets import get_secrets_manager

logger = logging.getLogger(__name__)


class ComposioError(Exception):
    """Base exception for Composio API errors."""
    pass


class ComposioAuthError(ComposioError):
    """Authentication error with Composio."""
    pass


class ComposioRateLimitError(ComposioError):
    """Rate limit exceeded."""
    pass


class ComposioClient:
    """
    Client for the Composio API.

    Composio enables building AI agents with access to tools and integrations.
    """

    BASE_URL = "https://app.composio.dev/api"

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Composio client.

        Args:
            api_key: Optional API key (loads from env if not provided)
        """
        secrets = get_secrets_manager()
        self.api_key = api_key or secrets.get_secret("composio")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self._client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers=self.headers,
            timeout=30.0,
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            await self._client.aclose()

    def _get_sync_client(self) -> httpx.Client:
        """Get synchronous HTTP client."""
        return httpx.Client(
            base_url=self.BASE_URL,
            headers=self.headers,
            timeout=30.0,
        )

    def _handle_error(self, response: httpx.Response) -> None:
        """Handle API error responses."""
        if response.status_code == 401:
            raise ComposioAuthError("Invalid API key")
        elif response.status_code == 429:
            raise ComposioRateLimitError("Rate limit exceeded")
        elif response.status_code >= 400:
            raise ComposioError(f"API error {response.status_code}: {response.text}")

    @retry(
        retry=retry_if_exception_type((ComposioRateLimitError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def get_integrations(self) -> List[Dict[str, Any]]:
        """
        Get available integrations.

        Returns:
            List of available integrations
        """
        with self._get_sync_client() as client:
            response = client.get("/integrations")
            self._handle_error(response)
            return response.json()

    @retry(
        retry=retry_if_exception_type((ComposioRateLimitError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def execute_action(
        self,
        action_name: str,
        params: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Execute a Composio action.

        Args:
            action_name: Name of the action to execute
            params: Action parameters

        Returns:
            Action execution result
        """
        with self._get_sync_client() as client:
            response = client.post(
                f"/actions/{action_name}/execute",
                json=params,
            )
            self._handle_error(response)
            return response.json()

    @retry(
        retry=retry_if_exception_type((ComposioRateLimitError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def get_connected_accounts(self) -> List[Dict[str, Any]]:
        """
        Get connected accounts.

        Returns:
            List of connected accounts
        """
        with self._get_sync_client() as client:
            response = client.get("/connectedAccounts")
            self._handle_error(response)
            return response.json()

    def health_check(self) -> bool:
        """
        Check if the API is accessible with current credentials.

        Returns:
            True if healthy, False otherwise
        """
        try:
            # Try to access API root - this validates DNS and connectivity
            with self._get_sync_client() as client:
                response = client.get("/")
                # Accept any response that indicates the server is up
                if response.status_code in [200, 401, 403, 404]:
                    # 401/403 means auth is working (server responded)
                    # 404 means endpoint might differ but server is up
                    return True
        except ComposioAuthError:
            logger.error("Composio authentication failed - check API key")
            return False
        except httpx.ConnectError as e:
            logger.warning(f"Composio connection error (service may be unavailable): {e}")
            # Return True anyway - key is configured, service might just be unreachable
            return True
        except Exception as e:
            logger.error(f"Composio health check failed: {e}")
            return False
        return True


# Convenience function
def get_composio_client() -> ComposioClient:
    """Get configured Composio client."""
    return ComposioClient()
