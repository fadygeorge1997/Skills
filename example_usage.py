#!/usr/bin/env python3
"""
Example usage of the API integrations package.

Demonstrates various use cases and patterns.
"""

import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def example_basic_usage():
    """Example: Basic usage with unified manager."""
    print("\n" + "=" * 60)
    print("Example: Basic Usage")
    print("=" * 60)

    from api_integrations import APIManager

    # Initialize manager
    manager = APIManager()

    # Generate text (auto-selects provider based on health)
    try:
        response = manager.generate_text(
            "What is the capital of France?",
            provider="gemini"
        )
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")


def example_individual_clients():
    """Example: Using individual clients."""
    print("\n" + "=" * 60)
    print("Example: Individual Clients")
    print("=" * 60)

    from api_integrations.gemini_client import get_gemini_client
    from api_integrations.minimax_client import get_minimax_client

    # Gemini
    try:
        gemini = get_gemini_client()
        response = gemini.generate_text("Explain Python decorators")
        print(f"Gemini: {response[:200]}...")
    except Exception as e:
        print(f"Gemini error: {e}")

    # Minimax
    try:
        minimax = get_minimax_client()
        response = minimax.generate_text("什么是机器学习？")
        print(f"Minimax: {response[:200]}...")
    except Exception as e:
        print(f"Minimax error: {e}")


def example_chat_completion():
    """Example: Chat completion with Minimax."""
    print("\n" + "=" * 60)
    print("Example: Chat Completion")
    print("=" * 60)

    from api_integrations.minimax_client import get_minimax_client

    client = get_minimax_client()

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the benefits of exercise?"},
    ]

    try:
        response = client.chat_completion(
            messages=messages,
            temperature=0.7,
            max_tokens=200,
        )
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")


def example_list_models():
    """Example: List available models."""
    print("\n" + "=" * 60)
    print("Example: List Models")
    print("=" * 60)

    from api_integrations.gemini_client import get_gemini_client

    client = get_gemini_client()

    try:
        models = client.list_models()
        print(f"Available Gemini models ({len(models)}):")
        for model in models[:5]:
            name = model.get('name', 'unknown').split('/')[-1]
            print(f"  - {name}")
    except Exception as e:
        print(f"Error: {e}")


def example_langsmith_setup():
    """Example: Setup LangSmith tracing."""
    print("\n" + "=" * 60)
    print("Example: LangSmith Tracing Setup")
    print("=" * 60)

    from api_integrations.langsmith_client import get_langsmith_client

    client = get_langsmith_client()

    # Setup environment for automatic tracing
    client.setup_tracing()

    print("✓ LangSmith tracing configured")
    print(f"  Project: {client.project}")
    print(f"  Endpoint: {client.endpoint}")

    # List projects
    try:
        projects = client.list_projects()
        print(f"\nAvailable projects ({len(projects)}):")
        for proj in projects:
            print(f"  - {proj.get('name', 'unknown')}")
    except Exception as e:
        print(f"Error listing projects: {e}")


def example_secrets_management():
    """Example: Secrets management."""
    print("\n" + "=" * 60)
    print("Example: Secrets Management")
    print("=" * 60)

    from api_integrations.secrets import get_secrets_manager

    secrets = get_secrets_manager()

    # Show masked keys
    print("API Keys (masked):")
    for name in ["composio", "langsmith", "minimax", "gemini"]:
        print(f"  {name}: {secrets.mask_secret(name)}")

    # Validate all secrets
    print("\nValidation:")
    validation = secrets.validate_all_secrets()
    for name, is_valid in validation.items():
        status = "✓" if is_valid else "✗"
        print(f"  {status} {name}")

    # Usage report
    print("\nUsage Report:")
    report = secrets.get_usage_report()
    for name, meta in report["secrets"].items():
        print(f"  {name}: {meta['use_count']} uses")


def example_error_handling():
    """Example: Error handling."""
    print("\n" + "=" * 60)
    print("Example: Error Handling")
    print("=" * 60)

    from api_integrations.errors import ErrorBoundary, safe_execute

    # Using ErrorBoundary context manager
    with ErrorBoundary(fallback="default_value"):
        # This might fail
        result = "success"  # Replace with risky operation
        print(f"Result: {result}")

    # Using safe_execute
    def risky_operation():
        # Simulated risk
        return "operation_result"

    result = safe_execute(
        risky_operation,
        fallback="fallback_value",
        error_message="Operation failed",
    )
    print(f"Safe result: {result}")


def example_health_check():
    """Example: Health monitoring."""
    print("\n" + "=" * 60)
    print("Example: Health Check")
    print("=" * 60)

    from api_integrations import APIManager

    manager = APIManager()

    health = manager.health_check_all()

    print("Service Health:")
    for service, status in health.items():
        icon = "✅" if status else "❌"
        state = "healthy" if status else "unhealthy"
        print(f"  {icon} {service}: {state}")


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("API Integrations - Usage Examples")
    print("=" * 60)

    examples = [
        ("Basic Usage", example_basic_usage),
        ("Individual Clients", example_individual_clients),
        ("Chat Completion", example_chat_completion),
        ("List Models", example_list_models),
        ("LangSmith Setup", example_langsmith_setup),
        ("Secrets Management", example_secrets_management),
        ("Error Handling", example_error_handling),
        ("Health Check", example_health_check),
    ]

    for name, func in examples:
        try:
            func()
        except Exception as e:
            print(f"\n❌ {name} failed: {e}")

    print("\n" + "=" * 60)
    print("Examples completed")
    print("=" * 60)


if __name__ == "__main__":
    main()
