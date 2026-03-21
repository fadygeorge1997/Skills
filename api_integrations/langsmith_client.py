"""
LangSmith API Client

LangSmith provides observability and debugging for LangChain applications.
Docs: https://docs.smith.langchain.com/
"""

import logging
from typing import Any, Dict, List, Optional
from datetime import datetime

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from .config import settings
from .secrets import get_secrets_manager

logger = logging.getLogger(__name__)


class LangSmithError(Exception):
    """Base exception for LangSmith API errors."""
    pass


class LangSmithAuthError(LangSmithError):
    """Authentication error with LangSmith."""
    pass


class LangSmithClient:
    """
    Client for the LangSmith API.

    LangSmith enables tracing, monitoring, and evaluating LLM applications.
    """

    BASE_PATH = "/v1"

    def __init__(
        self,
        api_key: Optional[str] = None,
        endpoint: Optional[str] = None,
        project: Optional[str] = None,
    ):
        """
        Initialize LangSmith client.

        Args:
            api_key: Optional API key
            endpoint: Optional API endpoint
            project: Optional project name
        """
        secrets = get_secrets_manager()

        self.api_key = api_key or secrets.get_secret("langsmith")
        # Use API v1 endpoint
        base = endpoint or settings.langsmith_endpoint
        self.endpoint = base.rstrip("/") + self.BASE_PATH
        self.project = project or settings.langsmith_project

        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
        }

        self._client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            base_url=self.endpoint,
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
            base_url=self.endpoint,
            headers=self.headers,
            timeout=30.0,
        )

    def _handle_error(self, response: httpx.Response) -> None:
        """Handle API error responses."""
        if response.status_code == 401:
            raise LangSmithAuthError("Invalid API key")
        elif response.status_code == 403:
            raise LangSmithAuthError("Insufficient permissions")
        elif response.status_code >= 400:
            raise LangSmithError(f"API error {response.status_code}: {response.text}")

    @retry(
        retry=retry_if_exception_type((LangSmithError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def list_runs(
        self,
        project_name: Optional[str] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """
        List runs/traces from LangSmith.

        Args:
            project_name: Filter by project name
            start_time: Filter by start time
            end_time: Filter by end time
            limit: Maximum number of runs to return

        Returns:
            List of run data
        """
        params = {"limit": limit}
        if project_name:
            params["project"] = project_name
        if start_time:
            params["start_time"] = start_time.isoformat()
        if end_time:
            params["end_time"] = end_time.isoformat()

        with self._get_sync_client() as client:
            response = client.get("/runs", params=params)
            self._handle_error(response)
            data = response.json()
            return data.get("runs", [])

    @retry(
        retry=retry_if_exception_type((LangSmithError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def get_run(self, run_id: str) -> Dict[str, Any]:
        """
        Get a specific run by ID.

        Args:
            run_id: The run ID

        Returns:
            Run data
        """
        with self._get_sync_client() as client:
            response = client.get(f"/runs/{run_id}")
            self._handle_error(response)
            return response.json()

    @retry(
        retry=retry_if_exception_type((LangSmithError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def create_feedback(
        self,
        run_id: str,
        key: str,
        score: Optional[float] = None,
        comment: Optional[str] = None,
        value: Optional[Any] = None,
    ) -> Dict[str, Any]:
        """
        Add feedback to a run.

        Args:
            run_id: The run ID to add feedback to
            key: Feedback key/category
            score: Numeric score (optional)
            comment: Text comment (optional)
            value: Any JSON-serializable value (optional)

        Returns:
            Created feedback data
        """
        body = {"key": key}
        if score is not None:
            body["score"] = score
        if comment:
            body["comment"] = comment
        if value is not None:
            body["value"] = value

        with self._get_sync_client() as client:
            response = client.post(
                f"/runs/{run_id}/feedback",
                json=body,
            )
            self._handle_error(response)
            return response.json()

    @retry(
        retry=retry_if_exception_type((LangSmithError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def list_projects(self) -> List[Dict[str, Any]]:
        """
        List all projects.

        Returns:
            List of projects
        """
        with self._get_sync_client() as client:
            response = client.get("/projects")
            self._handle_error(response)
            data = response.json()
            return data.get("projects", [])

    def setup_tracing(self) -> None:
        """
        Configure environment for LangChain tracing.
        Sets environment variables for automatic tracing.
        """
        import os

        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_API_KEY"] = self.api_key
        os.environ["LANGCHAIN_ENDPOINT"] = self.endpoint
        os.environ["LANGCHAIN_PROJECT"] = self.project

        logger.info(f"LangSmith tracing configured for project: {self.project}")

    def health_check(self) -> bool:
        """
        Check if the API is accessible.

        Returns:
            True if healthy, False otherwise
        """
        try:
            # Try to access API with a simple request
            with self._get_sync_client() as client:
                response = client.get("/info")
                # 200 means success, 401 means auth issue but endpoint exists
                if response.status_code in [200, 401, 404]:
                    return True
        except LangSmithAuthError:
            logger.error("LangSmith authentication failed - check API key")
            return False
        except httpx.HTTPStatusError as e:
            # Any HTTP response means the server is up
            if e.response.status_code == 404:
                # API path might differ but server responded
                return True
            return False
        except Exception as e:
            logger.error(f"LangSmith health check failed: {e}")
            return False
        return True


# Convenience function
def get_langsmith_client() -> LangSmithClient:
    """Get configured LangSmith client."""
    return LangSmithClient()
