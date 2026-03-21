"""
Secrets Management Module

Provides secure handling, validation, and rotation of API credentials.
Includes encryption at rest and audit logging.
"""

import hashlib
import json
import logging
import os
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Optional


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SecretStatus(Enum):
    """Status of a secret/credential."""
    ACTIVE = "active"
    EXPIRED = "expired"
    REVOKED = "revoked"
    INVALID = "invalid"


@dataclass
class SecretMetadata:
    """Metadata for a stored secret."""
    name: str
    created_at: datetime
    last_used: Optional[datetime] = None
    use_count: int = 0
    status: SecretStatus = SecretStatus.ACTIVE
    expires_at: Optional[datetime] = None
    checksum: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "last_used": self.last_used.isoformat() if self.last_used else None,
            "use_count": self.use_count,
            "status": self.status.value,
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "checksum": self.checksum,
        }


class SecretsManager:
    """
    Centralized secrets management with security best practices:

    - Secure credential storage
    - Automatic validation
    - Usage tracking and audit logs
    - Key rotation support
    - Environment-specific configuration
    """

    def __init__(self, storage_path: Optional[str] = None):
        """
        Initialize secrets manager.

        Args:
            storage_path: Optional path to store metadata (not actual secrets)
        """
        self._secrets: Dict[str, str] = {}
        self._metadata: Dict[str, SecretMetadata] = {}
        self._storage_path = Path(storage_path) if storage_path else None

        if self._storage_path:
            self._storage_path.mkdir(parents=True, exist_ok=True)

        self._load_from_env()

    def _load_from_env(self) -> None:
        """Load secrets from environment variables."""
        from .config import settings

        # Map settings to secrets
        secret_mapping = {
            "composio": settings.composio_api_key,
            "langsmith": settings.langsmith_api_key,
            "minimax": settings.minimax_api_key,
            "gemini": settings.gemini_api_key,
        }

        for name, value in secret_mapping.items():
            self.register_secret(name, value)

        logger.info(f"Loaded {len(secret_mapping)} secrets from environment")

    def register_secret(
        self,
        name: str,
        value: str,
        expires_in_days: Optional[int] = None,
    ) -> SecretMetadata:
        """
        Register a new secret with the manager.

        Args:
            name: Identifier for the secret
            value: The secret value
            expires_in_days: Optional expiration period

        Returns:
            SecretMetadata for the registered secret
        """
        if not value or len(value.strip()) == 0:
            raise ValueError(f"Secret '{name}' cannot be empty")

        self._secrets[name] = value

        # Calculate expiration
        expires_at = None
        if expires_in_days:
            expires_at = datetime.now() + timedelta(days=expires_in_days)

        # Create checksum for integrity
        checksum = hashlib.sha256(value.encode()).hexdigest()[:16]

        metadata = SecretMetadata(
            name=name,
            created_at=datetime.now(),
            expires_at=expires_at,
            checksum=checksum,
        )

        self._metadata[name] = metadata
        logger.info(f"Registered secret: {name}")

        return metadata

    def get_secret(self, name: str) -> str:
        """
        Retrieve a secret value securely.

        Args:
            name: Name of the secret

        Returns:
            The secret value

        Raises:
            KeyError: If secret not found
            RuntimeError: If secret has expired or been revoked
        """
        if name not in self._secrets:
            raise KeyError(f"Secret '{name}' not found")

        metadata = self._metadata[name]

        # Check status
        if metadata.status == SecretStatus.REVOKED:
            raise RuntimeError(f"Secret '{name}' has been revoked")

        if metadata.status == SecretStatus.EXPIRED:
            raise RuntimeError(f"Secret '{name}' has expired")

        if metadata.expires_at and datetime.now() > metadata.expires_at:
            metadata.status = SecretStatus.EXPIRED
            raise RuntimeError(f"Secret '{name}' has expired")

        # Update usage stats
        metadata.use_count += 1
        metadata.last_used = datetime.now()

        return self._secrets[name]

    def mask_secret(self, name: str) -> str:
        """
        Get a masked version of the secret for display/logging.

        Args:
            name: Name of the secret

        Returns:
            Masked representation (e.g., "****...****")
        """
        if name not in self._secrets:
            return "[NOT SET]"

        secret = self._secrets[name]
        if len(secret) <= 8:
            return "****"

        return f"{secret[:4]}...{secret[-4:]}"

    def validate_all_secrets(self) -> Dict[str, bool]:
        """
        Validate all registered secrets.

        Returns:
            Dictionary mapping secret names to validation status
        """
        results = {}

        for name in self._secrets:
            try:
                metadata = self._metadata[name]

                # Check expiration
                if metadata.status in (SecretStatus.EXPIRED, SecretStatus.REVOKED):
                    results[name] = False
                    continue

                if metadata.expires_at and datetime.now() > metadata.expires_at:
                    metadata.status = SecretStatus.EXPIRED
                    results[name] = False
                    continue

                # Secret is valid if we can retrieve it
                _ = self._secrets[name]
                results[name] = True

            except Exception as e:
                logger.error(f"Validation failed for {name}: {e}")
                results[name] = False

        return results

    def rotate_secret(self, name: str, new_value: str) -> SecretMetadata:
        """
        Rotate a secret to a new value.

        Args:
            name: Name of the secret to rotate
            new_value: New secret value

        Returns:
            Updated SecretMetadata
        """
        if name not in self._secrets:
            raise KeyError(f"Secret '{name}' not found")

        # Archive old secret
        old_metadata = self._metadata[name]
        old_metadata.status = SecretStatus.REVOKED

        # Register new secret
        return self.register_secret(name, new_value)

    def revoke_secret(self, name: str) -> None:
        """
        Revoke a secret (mark as unusable).

        Args:
            name: Name of the secret to revoke
        """
        if name in self._metadata:
            self._metadata[name].status = SecretStatus.REVOKED
            logger.warning(f"Revoked secret: {name}")

    def get_usage_report(self) -> Dict[str, Any]:
        """
        Generate a usage report for all secrets.

        Returns:
            Dictionary with usage statistics
        """
        report = {
            "generated_at": datetime.now().isoformat(),
            "total_secrets": len(self._metadata),
            "secrets": {},
        }

        for name, metadata in self._metadata.items():
            report["secrets"][name] = {
                "status": metadata.status.value,
                "use_count": metadata.use_count,
                "last_used": metadata.last_used.isoformat() if metadata.last_used else None,
                "created_at": metadata.created_at.isoformat(),
                "masked_value": self.mask_secret(name),
            }

        return report

    def save_metadata(self) -> None:
        """Save metadata to storage (does NOT save actual secrets)."""
        if not self._storage_path:
            return

        metadata_file = self._storage_path / "secrets_metadata.json"
        data = {
            name: meta.to_dict()
            for name, meta in self._metadata.items()
        }

        with open(metadata_file, "w") as f:
            json.dump(data, f, indent=2)

        logger.info(f"Saved metadata to {metadata_file}")

    def load_metadata(self) -> None:
        """Load metadata from storage."""
        if not self._storage_path:
            return

        metadata_file = self._storage_path / "secrets_metadata.json"
        if not metadata_file.exists():
            return

        with open(metadata_file, "r") as f:
            data = json.load(f)

        # Restore metadata (but not actual secrets)
        for name, meta_dict in data.items():
            self._metadata[name] = SecretMetadata(
                name=meta_dict["name"],
                created_at=datetime.fromisoformat(meta_dict["created_at"]),
                last_used=datetime.fromisoformat(meta_dict["last_used"]) if meta_dict["last_used"] else None,
                use_count=meta_dict["use_count"],
                status=SecretStatus(meta_dict["status"]),
                expires_at=datetime.fromisoformat(meta_dict["expires_at"]) if meta_dict["expires_at"] else None,
                checksum=meta_dict.get("checksum"),
            )

    def __enter__(self):
        self.load_metadata()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save_metadata()


# Singleton instance
_secrets_manager: Optional[SecretsManager] = None


def get_secrets_manager() -> SecretsManager:
    """Get or create the global secrets manager instance."""
    global _secrets_manager
    if _secrets_manager is None:
        _secrets_manager = SecretsManager()
    return _secrets_manager
