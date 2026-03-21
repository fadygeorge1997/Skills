# API Integrations

Centralized management for multiple AI service APIs with secure secrets handling, error recovery, and unified interface.

## Supported Services

| Service | Purpose | Docs |
|---------|---------|------|
| **Composio** | AI agent platform | [docs](https://docs.composio.io/) |
| **LangSmith** | LLM observability | [docs](https://docs.smith.langchain.com/) |
| **Minimax** | Chinese LLM API | [docs](https://platform.minimaxi.com/) |
| **Gemini** | Google's generative AI | [docs](https://ai.google.dev/) |

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your actual API keys
```

### 3. Run Tests

```bash
python test_integrations.py
```

### 4. Use CLI

```bash
# Show status
python cli.py status

# Generate text
python cli.py generate -p gemini "Hello, world!"

# Validate all keys
python cli.py validate
```

## Usage Examples

### Basic Usage

```python
from api_integrations import APIManager

# Initialize manager
manager = APIManager()

# Generate text with automatic provider selection
response = manager.generate_text("Explain quantum computing")

# Use specific provider
response = manager.minimax.generate_text("你好，世界")

# Check all service health
health = manager.health_check_all()
```

### Using Individual Clients

```python
from api_integrations.gemini_client import get_gemini_client

client = get_gemini_client()
response = client.generate_text("Tell me a joke")

# List available models
models = client.list_models()
```

### LangSmith Tracing

```python
from api_integrations.langsmith_client import LangSmithClient

client = LangSmithClient()
client.setup_tracing()

# Now all LangChain calls are automatically traced
```

### Minimax Chat

```python
from api_integrations.minimax_client import get_minimax_client

client = get_minimax_client()
response = client.chat_completion([
    {"role": "user", "content": "Hello"}
])
```

### Composio Actions

```python
from api_integrations.composio_client import ComposioClient

client = ComposioClient()
integrations = client.get_integrations()
```

## Project Structure

```
.
├── .env                          # Environment variables (gitignored)
├── .env.example                  # Environment template
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── cli.py                        # Command-line interface
├── test_integrations.py          # Integration tests
├── api_integrations/             # Main package
│   ├── __init__.py              # Package exports
│   ├── config.py                # Configuration management
│   ├── manager.py               # Unified API manager
│   ├── secrets.py               # Secrets management
│   ├── errors.py                # Error handling
│   ├── composio_client.py       # Composio integration
│   ├── langsmith_client.py      # LangSmith integration
│   ├── minimax_client.py        # Minimax integration
│   └── gemini_client.py         # Gemini integration
└── README.md                     # This file
```

## Configuration

All configuration is managed through environment variables:

```bash
# Composio
COMPOSIO_API_KEY=ak_...

# LangSmith
LANGSMITH_API_KEY=lsv2_...
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_PROJECT=default

# Minimax
MINIMAX_API_KEY=sk-api-...
MINIMAX_BASE_URL=https://api.minimaxi.chat

# Gemini
GEMINI_API_KEY=AIza...
GEMINI_MODEL=gemini-2.0-flash
```

## Security

### Secrets Management

- API keys are never logged in full
- Keys are masked in logs (e.g., `AIza...xxxx`)
- Secrets are validated on load
- Usage tracking for audit
- Support for key rotation

### Best Practices

```python
# Never do this:
print(f"API Key: {api_key}")  # ❌ Exposes full key

# Do this instead:
from api_integrations.secrets import get_secrets_manager
secrets = get_secrets_manager()
print(f"API Key: {secrets.mask_secret('gemini')}")  # ✅ AIza...xxxx
```

## Error Handling

All clients include automatic retry logic:

- Exponential backoff for rate limits
- Automatic retries for timeouts
- Circuit breaker pattern for failures

```python
from api_integrations.errors import ErrorBoundary

with ErrorBoundary(fallback="default_value"):
    result = risky_api_call()
```

## Health Monitoring

Check service health:

```python
from api_integrations import APIManager

manager = APIManager()
health = manager.health_check_all()

# Returns: {'composio': True, 'langsmith': True, ...}
```

## Troubleshooting

### API Key Issues

```bash
# Validate all keys
python cli.py validate

# Check specific service
python test_integrations.py --service gemini
```

### Rate Limits

All clients automatically retry with exponential backoff when rate limited.

### Timeouts

Increase timeout for slow operations:

```python
from api_integrations.minimax_client import MinimaxClient

client = MinimaxClient()
# Timeout is configured in the client class
```

## License

MIT
