# Key Management

## Principle

Secrets must not be committed to the repository.

Gateway v1 should load credentials from environment variables and local `.env` files during development.

## Provider Keys

Recommended environment variable pattern:

```text
OPENAI_API_KEY=
OPENROUTER_API_KEY=
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
```

## Gateway Auth

Gateway auth should be separate from provider auth.

```text
AGENTFORGE_GATEWAY_API_KEY=
```

Clients authenticate to the gateway with the gateway key. The gateway authenticates to providers with provider keys.

The OpenRouter adapter reads its key from `OPENROUTER_API_KEY` by default. Config files can override the environment variable name with `api_key_env`.

## Redaction Rules

- never log provider API keys
- never log gateway API keys
- redact authorization headers
- disable prompt and completion logging by default

## Future Work

- encrypted local key store
- team secret manager integrations
- per-client gateway keys
- key rotation workflow
