# Gateway V1 Architecture

## Summary

Gateway v1 is a small HTTP service that accepts OpenAI-compatible requests, resolves the requested model to a provider, sends the request through a provider adapter, and returns a normalized response.

## Components

### HTTP API

The public interface exposed to clients. V1 starts with OpenAI-compatible endpoints because many AI tools already support that API shape.

### Request Validator

Validates request shape, required fields, model names, streaming flags, and unsupported options before provider execution.

### Model Registry

Maps public model aliases to provider-specific model identifiers.

Example:

```yaml
models:
  gpt-4o-mini:
    provider: openai
    provider_model: gpt-4o-mini
  local-qwen:
    provider: ollama
    provider_model: qwen2.5-coder
```

### Router

Chooses the provider adapter for a request. V1 routing should stay simple: explicit model alias routing first, then optional fallback rules later.

### Provider Adapters

Provider-specific modules that translate normalized requests into provider calls and normalize provider responses.

### Key Manager

Loads provider credentials from environment variables or local configuration. V1 should not persist secrets in the repository.

### Observability Layer

Provides structured logs and basic request metadata. Prompt and completion logging must be disabled by default.

## Request Flow

1. Client sends an OpenAI-compatible request.
2. HTTP API authenticates the request if gateway auth is enabled.
3. Request Validator checks shape and supported options.
4. Model Registry resolves the model alias.
5. Router selects the provider adapter.
6. Adapter calls the provider.
7. Gateway normalizes and returns the response.

## V1 Boundary

V1 should optimize for clarity, local development, and compatibility. Advanced scheduling, multi-tenant billing, distributed queues, and persistent memory belong in later phases.
