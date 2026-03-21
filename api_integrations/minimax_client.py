"""
Minimax API Client

Minimax is a Chinese AI company providing LLM APIs.
Docs: https://platform.minimaxi.com/
"""

import json
import logging
from typing import Any, AsyncGenerator, Dict, List, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from .config import settings
from .secrets import get_secrets_manager

logger = logging.getLogger(__name__)


class MinimaxError(Exception):
    """Base exception for Minimax API errors."""
    pass


class MinimaxAuthError(MinimaxError):
    """Authentication error with Minimax."""
    pass


class MinimaxRateLimitError(MinimaxError):
    """Rate limit exceeded."""
    pass


class MinimaxClient:
    """
    Client for the Minimax API.

    Minimax provides text generation, embeddings, and other AI services.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        """
        Initialize Minimax client.

        Args:
            api_key: Optional API key
            base_url: Optional custom base URL
        """
        secrets = get_secrets_manager()
        self.api_key = api_key or secrets.get_secret("minimax")
        self.base_url = base_url or settings.minimax_base_url

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        self._client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            headers=self.headers,
            timeout=60.0,
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            await self._client.aclose()

    def _get_sync_client(self) -> httpx.Client:
        """Get synchronous HTTP client."""
        return httpx.Client(
            base_url=self.base_url,
            headers=self.headers,
            timeout=60.0,
        )

    def _handle_error(self, response: httpx.Response) -> None:
        """Handle API error responses."""
        try:
            error_data = response.json()
            error_msg = error_data.get("message", response.text)
        except Exception:
            error_msg = response.text

        if response.status_code == 401:
            raise MinimaxAuthError(f"Authentication failed: {error_msg}")
        elif response.status_code == 429:
            raise MinimaxRateLimitError(f"Rate limit exceeded: {error_msg}")
        elif response.status_code >= 400:
            raise MinimaxError(f"API error {response.status_code}: {error_msg}")

    @retry(
        retry=retry_if_exception_type((MinimaxRateLimitError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "abab6.5s-chat",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        stream: bool = False,
    ) -> Union[Dict[str, Any], Any]:
        """
        Create a chat completion.

        Args:
            messages: List of message dicts with 'role' and 'content'
            model: Model name to use
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens to generate
            stream: Whether to stream the response

        Returns:
            Completion response (dict for non-streaming, generator for streaming)
        """
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "stream": stream,
        }

        if max_tokens:
            payload["max_tokens"] = max_tokens

        with self._get_sync_client() as client:
            if stream:
                response = client.post(
                    "/v1/text/chatcompletion_v2",
                    json=payload,
                )
                self._handle_error(response)
                return self._parse_stream(response)
            else:
                response = client.post(
                    "/v1/text/chatcompletion_v2",
                    json=payload,
                )
                self._handle_error(response)
                return response.json()

    def _parse_stream(self, response: httpx.Response) -> Any:
        """Parse streaming response."""
        for line in response.iter_lines():
            if line.startswith("data: "):
                data = line[6:]
                if data == "[DONE]":
                    break
                try:
                    yield json.loads(data)
                except json.JSONDecodeError:
                    logger.warning(f"Failed to parse stream data: {data}")

    @retry(
        retry=retry_if_exception_type((MinimaxRateLimitError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def embeddings(
        self,
        texts: List[str],
        model: str = "embo-01",
        type_: str = "db",
    ) -> Dict[str, Any]:
        """
        Create embeddings for texts.

        Args:
            texts: List of texts to embed
            model: Embedding model name
            type_: Type of embedding ('db' or 'query')

        Returns:
            Embeddings response
        """
        payload = {
            "model": model,
            "texts": texts,
            "type": type_,
        }

        with self._get_sync_client() as client:
            response = client.post(
                "/v1/embeddings",
                json=payload,
            )
            self._handle_error(response)
            return response.json()

    def generate_text(
        self,
        prompt: str,
        model: str = "abab6.5s-chat",
        **kwargs
    ) -> str:
        """
        Simple text generation helper.

        Args:
            prompt: The prompt text
            model: Model to use
            **kwargs: Additional parameters

        Returns:
            Generated text
        """
        messages = [{"role": "user", "content": prompt}]
        response = self.chat_completion(messages, model=model, **kwargs)

        if isinstance(response, dict):
            choices = response.get("choices", [])
            if choices:
                return choices[0].get("message", {}).get("content", "")
        return ""

    def health_check(self) -> bool:
        """
        Check if the API is accessible.

        Returns:
            True if healthy, False otherwise
        """
        try:
            # Simple test request
            self.chat_completion(
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=5,
            )
            return True
        except MinimaxAuthError:
            logger.error("Minimax authentication failed - check API key")
            return False
        except Exception as e:
            logger.error(f"Minimax health check failed: {e}")
            return False


# Convenience function
def get_minimax_client() -> MinimaxClient:
    """Get configured Minimax client."""
    return MinimaxClient()
