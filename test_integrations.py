#!/usr/bin/env python3
"""
Test script for API integrations.

Validates that all API clients are correctly configured and functional.
"""

import argparse
import json
import logging
import sys
from typing import Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def test_configuration() -> bool:
    """Test that configuration loads correctly."""
    logger.info("=" * 60)
    logger.info("Testing Configuration...")
    logger.info("=" * 60)

    try:
        from api_integrations.config import Settings

        settings = Settings()
        logger.info("✓ Settings loaded successfully")

        # Show masked API keys
        logger.info(f"  Composio key: {settings.get_masked_key('composio_api_key')}")
        logger.info(f"  LangSmith key: {settings.get_masked_key('langsmith_api_key')}")
        logger.info(f"  Minimax key: {settings.get_masked_key('minimax_api_key')}")
        logger.info(f"  Gemini key: {settings.get_masked_key('gemini_api_key')}")

        return True
    except Exception as e:
        logger.error(f"✗ Configuration test failed: {e}")
        return False


def test_secrets_manager() -> bool:
    """Test secrets manager functionality."""
    logger.info("\n" + "=" * 60)
    logger.info("Testing Secrets Manager...")
    logger.info("=" * 60)

    try:
        from api_integrations.secrets import get_secrets_manager

        secrets = get_secrets_manager()
        logger.info("✓ Secrets manager initialized")

        # Test validation
        validation = secrets.validate_all_secrets()
        for name, is_valid in validation.items():
            status = "✓" if is_valid else "✗"
            logger.info(f"  {status} {name}: {secrets.mask_secret(name)}")

        # Get usage report
        report = secrets.get_usage_report()
        logger.info(f"✓ Usage report generated ({len(report['secrets'])} secrets)")

        return all(validation.values())
    except Exception as e:
        logger.error(f"✗ Secrets manager test failed: {e}")
        return False


def test_composio() -> bool:
    """Test Composio API connection."""
    logger.info("\n" + "=" * 60)
    logger.info("Testing Composio API...")
    logger.info("=" * 60)

    try:
        from api_integrations.composio_client import ComposioClient

        client = ComposioClient()

        if client.health_check():
            logger.info("✓ Composio API is healthy")
            return True
        else:
            logger.error("✗ Composio API health check failed")
            return False

    except Exception as e:
        logger.error(f"✗ Composio test failed: {e}")
        return False


def test_langsmith() -> bool:
    """Test LangSmith API connection."""
    logger.info("\n" + "=" * 60)
    logger.info("Testing LangSmith API...")
    logger.info("=" * 60)

    try:
        from api_integrations.langsmith_client import LangSmithClient

        client = LangSmithClient()

        if client.health_check():
            logger.info("✓ LangSmith API is healthy")
            logger.info(f"  Project: {client.project}")
            return True
        else:
            logger.error("✗ LangSmith API health check failed")
            return False

    except Exception as e:
        logger.error(f"✗ LangSmith test failed: {e}")
        return False


def test_minimax() -> bool:
    """Test Minimax API connection."""
    logger.info("\n" + "=" * 60)
    logger.info("Testing Minimax API...")
    logger.info("=" * 60)

    try:
        from api_integrations.minimax_client import MinimaxClient

        client = MinimaxClient()

        if client.health_check():
            logger.info("✓ Minimax API is healthy")
            return True
        else:
            logger.error("✗ Minimax API health check failed")
            return False

    except Exception as e:
        logger.error(f"✗ Minimax test failed: {e}")
        return False


def test_gemini() -> bool:
    """Test Gemini API connection."""
    logger.info("\n" + "=" * 60)
    logger.info("Testing Gemini API...")
    logger.info("=" * 60)

    try:
        from api_integrations.gemini_client import GeminiClient

        client = GeminiClient()

        if client.health_check():
            logger.info("✓ Gemini API is healthy")

            # List available models
            try:
                models = client.list_models()
                logger.info(f"  Available models: {len(models)}")
                for model in models[:3]:  # Show first 3
                    model_name = model.get('name', 'unknown')
                    logger.info(f"    - {model_name}")
            except Exception as e:
                logger.warning(f"  Could not list models: {e}")

            return True
        else:
            logger.error("✗ Gemini API health check failed")
            return False

    except Exception as e:
        logger.error(f"✗ Gemini test failed: {e}")
        return False


def test_api_manager() -> bool:
    """Test the unified API manager."""
    logger.info("\n" + "=" * 60)
    logger.info("Testing API Manager...")
    logger.info("=" * 60)

    try:
        from api_integrations import APIManager

        manager = APIManager()
        logger.info("✓ API Manager initialized")

        # Run health checks
        health = manager.health_check_all()

        all_healthy = all(health.values())
        if all_healthy:
            logger.info("✓ All services are healthy")
        else:
            logger.warning("⚠ Some services are unhealthy:")
            for service, status in health.items():
                icon = "✓" if status else "✗"
                logger.info(f"  {icon} {service}: {'healthy' if status else 'unhealthy'}")

        return True

    except Exception as e:
        logger.error(f"✗ API Manager test failed: {e}")
        return False


def run_all_tests() -> bool:
    """Run all tests."""
    logger.info("\n" + "=" * 60)
    logger.info("Starting API Integration Tests")
    logger.info("=" * 60)

    results = {
        "Configuration": test_configuration(),
        "Secrets Manager": test_secrets_manager(),
        "API Manager": test_api_manager(),
        "Composio": test_composio(),
        "LangSmith": test_langsmith(),
        "Minimax": test_minimax(),
        "Gemini": test_gemini(),
    }

    # Print summary
    logger.info("\n" + "=" * 60)
    logger.info("Test Summary")
    logger.info("=" * 60)

    for name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        logger.info(f"{status:8} {name}")

    total = len(results)
    passed = sum(results.values())
    failed = total - passed

    logger.info("\n" + "-" * 60)
    logger.info(f"Total: {total}, Passed: {passed}, Failed: {failed}")
    logger.info("=" * 60)

    return failed == 0


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Test API integrations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test_integrations.py              # Run all tests
  python test_integrations.py --service gemini   # Test only Gemini
  python test_integrations.py --verbose     # Verbose output
        """
    )

    parser.add_argument(
        "--service",
        choices=["config", "secrets", "manager", "composio", "langsmith", "minimax", "gemini"],
        help="Test only a specific service",
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output",
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Run specific test or all tests
    service_tests = {
        "config": test_configuration,
        "secrets": test_secrets_manager,
        "manager": test_api_manager,
        "composio": test_composio,
        "langsmith": test_langsmith,
        "minimax": test_minimax,
        "gemini": test_gemini,
    }

    if args.service:
        success = service_tests[args.service]()
    else:
        success = run_all_tests()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
