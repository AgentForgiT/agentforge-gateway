# Provider Routing

## V1 Strategy

Gateway v1 uses explicit model alias routing.

Each public model name maps to one provider and one provider-specific model name.

```yaml
models:
  fast-coder:
    provider: openrouter
    provider_model: qwen/qwen-2.5-coder
  local-coder:
    provider: ollama
    provider_model: qwen2.5-coder
```

## Why Explicit Routing First

Explicit routing is easy to debug, easy to document, and safe for early users. More advanced routing can come after the baseline is trustworthy.

## Future Routing Modes

- fallback routing when a provider is unavailable
- cost-aware routing
- latency-aware routing
- task-aware routing
- policy-based routing for teams

## Adapter Boundary

Adapters should hide provider-specific request and response differences. The router should not know how OpenAI, OpenRouter, Ollama, or other providers format their native payloads.
