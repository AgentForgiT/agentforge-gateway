# Configuration

Gateway v1 should use a small declarative configuration file plus environment variables for secrets.

## Example

```yaml
server:
  host: 127.0.0.1
  port: 8080

models:
  fast-coder:
    provider: openrouter
    provider_model: qwen/qwen-2.5-coder
  local-coder:
    provider: ollama
    provider_model: qwen2.5-coder

providers:
  openrouter:
    base_url: https://openrouter.ai/api/v1
    api_key_env: OPENROUTER_API_KEY
  ollama:
    base_url: http://localhost:11434
```

## Rules

- configuration should be readable by humans
- secrets should be referenced by environment variable name
- invalid model aliases should fail at startup
- invalid provider configuration should fail at startup
