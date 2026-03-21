#!/usr/bin/env python3
"""
CLI Tool for API Integrations

Provides command-line interface for managing API integrations.
"""

import argparse
import json
import logging
import sys
from pathlib import Path

from api_integrations import APIManager
from api_integrations.config import get_settings
from api_integrations.secrets import get_secrets_manager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def cmd_status(args) -> int:
    """Show status of all integrations."""
    manager = APIManager()

    print("\n" + "=" * 70)
    print("API Integration Status")
    print("=" * 70)

    # Configuration
    print("\n📋 Configuration:")
    settings = get_settings()
    print(f"  Composio:    {settings.get_masked_key('composio_api_key')}")
    print(f"  LangSmith:   {settings.get_masked_key('langsmith_api_key')}")
    print(f"  Minimax:     {settings.get_masked_key('minimax_api_key')}")
    print(f"  Gemini:      {settings.get_masked_key('gemini_api_key')}")

    # Health checks
    print("\n🏥 Health Checks:")
    health = manager.health_check_all()
    for service, status in health.items():
        icon = "✅" if status else "❌"
        print(f"  {icon} {service.capitalize()}")

    # Secrets usage
    print("\n🔐 Secrets Usage:")
    secrets = get_secrets_manager()
    report = secrets.get_usage_report()
    for name, meta in report["secrets"].items():
        print(f"  {name}: {meta['use_count']} uses, status: {meta['status']}")

    print("\n" + "=" * 70)
    return 0


def cmd_generate(args) -> int:
    """Generate text using an AI provider."""
    manager = APIManager()

    provider = args.provider
    prompt = args.prompt

    print(f"\n🤖 Generating with {provider}...")
    print(f"Prompt: {prompt[:100]}{'...' if len(prompt) > 100 else ''}")
    print("-" * 70)

    try:
        response = manager.generate_text(prompt, provider=provider)
        print(response)
        return 0
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1


def cmd_validate(args) -> int:
    """Validate all API keys."""
    print("\n🔍 Validating API keys...")
    print("=" * 70)

    manager = APIManager()
    health = manager.health_check_all()

    all_valid = all(health.values())

    for service, status in health.items():
        if status:
            print(f"✅ {service.capitalize()}: Valid")
        else:
            print(f"❌ {service.capitalize()}: Invalid or unreachable")

    return 0 if all_valid else 1


def cmd_info(args) -> int:
    """Show detailed information about a service."""
    service = args.service
    manager = APIManager()

    print(f"\n📊 {service.capitalize()} Information")
    print("=" * 70)

    if service == "gemini":
        try:
            models = manager.gemini.list_models()
            print(f"\nAvailable Models ({len(models)}):")
            for model in models:
                name = model.get('name', 'unknown').split('/')[-1]
                display = model.get('displayName', name)
                print(f"  • {display}")
        except Exception as e:
            print(f"Error: {e}")

    elif service == "langsmith":
        try:
            projects = manager.langsmith.list_projects()
            print(f"\nProjects ({len(projects)}):")
            for proj in projects:
                print(f"  • {proj.get('name', 'unknown')}")
        except Exception as e:
            print(f"Error: {e}")

    return 0


def cmd_env(args) -> int:
    """Show environment setup instructions."""
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║              API Integration Environment Setup                        ║
╠══════════════════════════════════════════════════════════════════════╣

1. Create .env file from template:
   cp .env.example .env

2. Edit .env and add your actual API keys:
   - COMPOSIO_API_KEY=your_key_here
   - LANGSMITH_API_KEY=your_key_here
   - MINIMAX_API_KEY=your_key_here
   - GEMINI_API_KEY=your_key_here

3. Install dependencies:
   pip install -r requirements.txt

4. Verify setup:
   python test_integrations.py

5. Run CLI:
   python cli.py status

╚══════════════════════════════════════════════════════════════════════╝
    """)
    return 0


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="API Integrations CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py status                # Show all service statuses
  python cli.py validate              # Validate all API keys
  python cli.py generate -p gemini "Hello"  # Generate text
  python cli.py info gemini           # Show Gemini info
  python cli.py env                   # Show setup instructions
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Status command
    status_parser = subparsers.add_parser("status", help="Show integration status")
    status_parser.set_defaults(func=cmd_status)

    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Validate API keys")
    validate_parser.set_defaults(func=cmd_validate)

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate text")
    generate_parser.add_argument("prompt", help="Text prompt")
    generate_parser.add_argument(
        "-p", "--provider",
        choices=["gemini", "minimax", "auto"],
        default="auto",
        help="AI provider to use",
    )
    generate_parser.set_defaults(func=cmd_generate)

    # Info command
    info_parser = subparsers.add_parser("info", help="Show service information")
    info_parser.add_argument(
        "service",
        choices=["composio", "langsmith", "minimax", "gemini"],
        help="Service to show info for",
    )
    info_parser.set_defaults(func=cmd_info)

    # Env command
    env_parser = subparsers.add_parser("env", help="Show environment setup")
    env_parser.set_defaults(func=cmd_env)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
