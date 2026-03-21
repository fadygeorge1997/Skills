"""
Google Gemini API Client

Gemini is Google's generative AI model.
Docs: https://ai.google.dev/
"""

import logging
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional, Union

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from .config import settings
from .secrets import get_secrets_manager

logger = logging.getLogger(__name__)


class GeminiError(Exception):
    """Base exception for Gemini API errors."""
    pass


class GeminiAuthError(GeminiError):
    """Authentication error with Gemini."""
    pass


class GeminiRateLimitError(GeminiError):
    """Rate limit exceeded."""
    pass


class GeminiClient:
    """
    Client for the Google Gemini API.

    Gemini provides text generation, image understanding, and multimodal capabilities.
    """

    BASE_URL = "https://generativelanguage.googleapis.com/v1beta"

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
    ):
        """
        Initialize Gemini client.

        Args:
            api_key: Optional API key
            model: Optional model name
        """
        secrets = get_secrets_manager()
        self.api_key = api_key or secrets.get_secret("gemini")
        self.model = model or settings.gemini_model

        self._client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            timeout=60.0,
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            await self._client.aclose()

    def _get_sync_client(self) -> httpx.Client:
        """Get synchronous HTTP client."""
        return httpx.Client(
            base_url=self.BASE_URL,
            timeout=60.0,
        )

    def _get_auth_param(self) -> Dict[str, str]:
        """Get authentication query parameter."""
        return {"key": self.api_key}

    def _handle_error(self, response: httpx.Response) -> None:
        """Handle API error responses."""
        try:
            error_data = response.json()
            error_msg = error_data.get("error", {}).get("message", response.text)
        except Exception:
            error_msg = response.text

        if response.status_code == 400:
            raise GeminiError(f"Bad request: {error_msg}")
        elif response.status_code == 401 or response.status_code == 403:
            raise GeminiAuthError(f"Authentication failed: {error_msg}")
        elif response.status_code == 429:
            raise GeminiRateLimitError(f"Rate limit exceeded: {error_msg}")
        elif response.status_code >= 500:
            raise GeminiError(f"Server error {response.status_code}: {error_msg}")
        elif response.status_code >= 400:
            raise GeminiError(f"API error {response.status_code}: {error_msg}")

    @retry(
        retry=retry_if_exception_type((GeminiRateLimitError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def generate_content(
        self,
        contents: List[Dict[str, Any]],
        generation_config: Optional[Dict[str, Any]] = None,
        safety_settings: Optional[List[Dict[str, str]]] = None,
        stream: bool = False,
    ) -> Union[Dict[str, Any], Generator[Dict[str, Any], None, None]]:
        """
        Generate content using Gemini.

        Args:
            contents: List of content objects with 'role' and 'parts'
            generation_config: Optional generation parameters
            safety_settings: Optional safety settings
            stream: Whether to stream the response

        Returns:
            Generated content response
        """
        payload = {"contents": contents}

        if generation_config:
            payload["generationConfig"] = generation_config
        if safety_settings:
            payload["safetySettings"] = safety_settings

        params = self._get_auth_param()

        with self._get_sync_client() as client:
            response = client.post(
                f"models/{self.model}:generateContent",
                params=params,
                json=payload,
            )
            self._handle_error(response)
            return response.json()

    def generate_text(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_output_tokens: Optional[int] = None,
        **kwargs
    ) -> str:
        """
        Simple text generation helper.

        Args:
            prompt: The prompt text
            temperature: Sampling temperature (0-1)
            max_output_tokens: Maximum tokens to generate
            **kwargs: Additional parameters

        Returns:
            Generated text
        """
        contents = [{"role": "user", "parts": [{"text": prompt}]}]

        generation_config = {
            "temperature": temperature,
        }
        if max_output_tokens:
            generation_config["maxOutputTokens"] = max_output_tokens

        response = self.generate_content(
            contents=contents,
            generation_config=generation_config,
        )

        if isinstance(response, dict):
            candidates = response.get("candidates", [])
            if candidates:
                content = candidates[0].get("content", {})
                parts = content.get("parts", [])
                if parts:
                    return parts[0].get("text", "")
        return ""

    def generate_image(
        self,
        prompt: str,
        size: str = "1024x1024",
        quality: str = "standard",
        n: int = 1,
    ) -> Dict[str, Any]:
        """
        Generate image using Gemini (if model supports it).

        Args:
            prompt: Image generation prompt
            size: Image size
            quality: Image quality
            n: Number of images

        Returns:
            Image generation response
        """
        # Note: This uses the image generation capability
        # Adjust based on actual Gemini API for image generation
        contents = [{"role": "user", "parts": [{"text": prompt}]}]

        generation_config = {
            "responseModalities": ["IMAGE"],
        }

        response = self.generate_content(
            contents=contents,
            generation_config=generation_config,
        )

        return response

    def count_tokens(self, text: str) -> int:
        """
        Count tokens in text.

        Args:
            text: Text to count

        Returns:
            Token count
        """
        contents = [{"role": "user", "parts": [{"text": text}]}]
        params = self._get_auth_param()

        with self._get_sync_client() as client:
            response = client.post(
                f"models/{self.model}:countTokens",
                params=params,
                json={"contents": contents},
            )
            self._handle_error(response)
            data = response.json()
            return data.get("totalTokens", 0)

    @retry(
        retry=retry_if_exception_type((GeminiRateLimitError, httpx.TimeoutException)),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def list_models(self) -> List[Dict[str, Any]]:
        """
        List available models.

        Returns:
            List of available models
        """
        params = self._get_auth_param()

        with self._get_sync_client() as client:
            response = client.get(
                "models",
                params=params,
            )
            self._handle_error(response)
            data = response.json()
            return data.get("models", [])

    def health_check(self) -> bool:
        """
        Check if the API is accessible.

        Returns:
            True if healthy, False otherwise
        """
        try:
            self.list_models()
            return True
        except GeminiAuthError:
            logger.error("Gemini authentication failed - check API key")
            return False
        except Exception as e:
            logger.error(f"Gemini health check failed: {e}")
            return False


# Try to use the official Google library if available
try:
    import google.generativeai as genai

    class GeminiClientOfficial(GeminiClient):
        """
        Gemini client using the official Google library.
        Falls back to HTTP client if library not available.
        """

        def __init__(
            self,
            api_key: Optional[str] = None,
            model: Optional[str] = None,
        ):
            secrets = get_secrets_manager()
            self.api_key = api_key or secrets.get_secret("gemini")
            self.model = model or settings.gemini_model

            genai.configure(api_key=self.api_key)
            self._model = genai.GenerativeModel(self.model)

        def generate_text(
            self,
            prompt: str,
            temperature: float = 0.7,
            max_output_tokens: Optional[int] = None,
            **kwargs
        ) -> str:
            """Generate text using official SDK."""
            generation_config = genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_output_tokens,
            )

            response = self._model.generate_content(
                prompt,
                generation_config=generation_config,
            )

            return response.text

except ImportError:
    GeminiClientOfficial = GeminiClient


# Convenience function
def get_gemini_client(use_official: bool = True) -> GeminiClient:
    """Get configured Gemini client."""
    if use_official:
        try:
            import google.generativeai
            return GeminiClientOfficial()
        except ImportError:
            pass
    return GeminiClient()
