"""
Error handling module for API integrations.

Provides standardized error types and exception handling utilities.
"""

import logging
from typing import Any, Callable, Dict, Optional, Type, TypeVar

from tenacity import (
    RetryError,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

logger = logging.getLogger(__name__)

T = TypeVar("T")


class APIIntegrationError(Exception):
    """Base exception for API integration errors."""

    def __init__(self, message: str, original_error: Optional[Exception] = None):
        super().__init__(message)
        self.message = message
        self.original_error = original_error

    def __str__(self) -> str:
        if self.original_error:
            return f"{self.message} (caused by: {self.original_error})"
        return self.message


class ConfigurationError(APIIntegrationError):
    """Configuration-related error (missing env vars, invalid settings)."""
    pass


class AuthenticationError(APIIntegrationError):
    """Authentication failure (invalid API key, expired token)."""
    pass


class RateLimitError(APIIntegrationError):
    """Rate limit exceeded."""

    def __init__(
        self,
        message: str,
        retry_after: Optional[int] = None,
        original_error: Optional[Exception] = None,
    ):
        super().__init__(message, original_error)
        self.retry_after = retry_after


class TimeoutError(APIIntegrationError):
    """Request timeout."""
    pass


class ValidationError(APIIntegrationError):
    """Input validation error."""
    pass


class ServiceUnavailableError(APIIntegrationError):
    """Service temporarily unavailable."""
    pass


class IntegrationError(APIIntegrationError):
    """Generic integration error."""
    pass


def map_exception(
    original: Exception,
    context: str = "",
) -> APIIntegrationError:
    """
    Map a low-level exception to our standardized error types.

    Args:
        original: The original exception
        context: Additional context for the error

    Returns:
        Mapped APIIntegrationError
    """
    message = f"{context}: {str(original)}" if context else str(original)

    # Map by exception type
    if isinstance(original, ImportError):
        return ConfigurationError(f"Missing required dependency: {original}", original)

    # Map HTTP errors
    error_str = str(original).lower()

    if "unauthorized" in error_str or "401" in error_str:
        return AuthenticationError("Authentication failed", original)

    if "forbidden" in error_str or "403" in error_str:
        return AuthenticationError("Access denied", original)

    if "rate limit" in error_str or "429" in error_str:
        return RateLimitError("Rate limit exceeded", original_error=original)

    if "timeout" in error_str:
        return TimeoutError("Request timed out", original)

    if "unavailable" in error_str or "503" in error_str:
        return ServiceUnavailableError("Service unavailable", original)

    # Default
    return IntegrationError(message, original)


def safe_execute(
    func: Callable[..., T],
    *args,
    fallback: Optional[T] = None,
    error_message: str = "Operation failed",
    **kwargs,
) -> T:
    """
    Execute a function safely with error handling.

    Args:
        func: Function to execute
        *args: Function arguments
        fallback: Fallback value on error
        error_message: Message for error logging
        **kwargs: Function keyword arguments

    Returns:
        Function result or fallback value
    """
    try:
        return func(*args, **kwargs)
    except Exception as e:
        mapped = map_exception(e, error_message)
        logger.error(f"{error_message}: {mapped}")

        if fallback is not None:
            return fallback
        raise mapped


class ErrorBoundary:
    """
    Context manager for error boundaries.

    Catches and logs errors, optionally returning a fallback value.

    Example:
        with ErrorBoundary(fallback="default"):
            result = risky_operation()
    """

    def __init__(
        self,
        fallback: Optional[Any] = None,
        reraise: bool = False,
        log_level: str = "error",
    ):
        self.fallback = fallback
        self.reraise = reraise
        self.log_level = log_level
        self.error: Optional[Exception] = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.error = exc_val
            mapped = map_exception(exc_val)

            logger_method = getattr(logger, self.log_level)
            logger_method(f"Error in boundary: {mapped}")

            if self.reraise:
                raise mapped

            # Suppress exception and return fallback
            return True

    def has_error(self) -> bool:
        """Check if an error occurred."""
        return self.error is not None


def create_retry_decorator(
    max_attempts: int = 3,
    retryable_exceptions: tuple = (Exception,),
):
    """
    Create a retry decorator with custom settings.

    Args:
        max_attempts: Maximum retry attempts
        retryable_exceptions: Exception types to retry on

    Returns:
        Retry decorator
    """
    from tenacity import retry

    return retry(
        retry=retry_if_exception_type(retryable_exceptions),
        stop=stop_after_attempt(max_attempts),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True,
    )


class APIHealthMonitor:
    """
    Monitor health of API integrations.

    Tracks success/failure rates and provides circuit breaker functionality.
    """

    def __init__(self, failure_threshold: int = 5, reset_timeout: int = 60):
        """
        Initialize health monitor.

        Args:
            failure_threshold: Consecutive failures before circuit opens
            reset_timeout: Seconds before attempting reset
        """
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self._failure_counts: Dict[str, int] = {}
        self._circuit_states: Dict[str, str] = {}  # "closed", "open", "half-open"
        self._last_failure_time: Dict[str, float] = {}

    def record_success(self, service: str) -> None:
        """Record a successful request."""
        self._failure_counts[service] = 0
        self._circuit_states[service] = "closed"

    def record_failure(self, service: str) -> bool:
        """
        Record a failed request.

        Returns:
            True if circuit breaker is open
        """
        import time

        self._failure_counts[service] = self._failure_counts.get(service, 0) + 1
        self._last_failure_time[service] = time.time()

        if self._failure_counts[service] >= self.failure_threshold:
            self._circuit_states[service] = "open"
            logger.warning(f"Circuit breaker opened for {service}")
            return True

        return False

    def is_circuit_open(self, service: str) -> bool:
        """Check if circuit breaker is open for a service."""
        import time

        if service not in self._circuit_states:
            return False

        if self._circuit_states[service] == "open":
            # Check if we should try reset
            last_fail = self._last_failure_time.get(service, 0)
            if time.time() - last_fail > self.reset_timeout:
                self._circuit_states[service] = "half-open"
                logger.info(f"Circuit breaker half-open for {service}")
                return False
            return True

        return False

    def get_status(self, service: str) -> Dict[str, Any]:
        """Get health status for a service."""
        import time

        return {
            "service": service,
            "state": self._circuit_states.get(service, "closed"),
            "failure_count": self._failure_counts.get(service, 0),
            "threshold": self.failure_threshold,
            "last_failure": self._last_failure_time.get(service),
        }
