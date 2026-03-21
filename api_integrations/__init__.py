"""
API Integrations Package

Provides secure, centralized access to multiple AI services:
- Composio: AI agent platform
- LangSmith: LangChain observability
- Minimax: Chinese LLM API
- Gemini: Google's generative AI

Usage:
    from api_integrations import APIManager

    manager = APIManager()
    gemini_response = manager.gemini.generate_text("Hello")
"""

from .manager import APIManager
from .config import Settings
from .secrets import SecretsManager

__version__ = "1.0.0"
__all__ = ["APIManager", "Settings", "SecretsManager"]
