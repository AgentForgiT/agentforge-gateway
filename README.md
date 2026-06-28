# agentforge-gateway

> Historical prototype notice:
> Canonical gateway development has moved to `AgentForgiT/agentforge` under `apps/gateway`.
> This repository remains public to preserve prototype history, releases, and migration context.
> New gateway work should target the canonical monorepo unless a later accepted AgentForge decision says otherwise.

Universal AI gateway for the AgentForge ecosystem.

## Purpose

`agentforge-gateway` will provide one OpenAI-compatible entry point for multiple model providers, local models, agentic IDEs, and future AgentForge services.

The first version is intentionally architecture-first. Implementation starts only after the API, routing, configuration, and security model are documented.

## V1 Goals

- expose an OpenAI-compatible HTTP API
- route requests across multiple providers
- support free-tier and local model providers where practical
- centralize API key management
- provide a compatibility layer for agentic coding tools
- keep provider-specific logic isolated behind adapters

## Non-Goals

- building a custom model runtime
- replacing provider SDKs everywhere
- adding distributed infrastructure before local development works
- storing user prompts or completions by default

## Documentation

- [Overview](docs/overview.md)
- [V1 Architecture](docs/architecture-v1.md)
- [API Contract](docs/api-contract.md)
- [Provider Routing](docs/provider-routing.md)
- [Key Management](docs/key-management.md)
- [Compatibility Targets](docs/compatibility-targets.md)
- [Configuration](docs/configuration.md)

## Local MVP

The current MVP is a dependency-free Python service with a deterministic mock provider and an optional OpenRouter provider adapter.

Run tests:

```bash
python -m unittest discover -s tests
```

Run the gateway:

```bash
python -m agentforge_gateway.cli --config config.example.json
```

If running from a source checkout without installation, include `src` on `PYTHONPATH`:

```bash
PYTHONPATH=src python -m agentforge_gateway.cli --config config.example.json
```

Windows PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m agentforge_gateway.cli --config config.example.json
```

Call the mock chat endpoint:

```bash
curl http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mock-coder",
    "messages": [
      { "role": "user", "content": "Write a Python function." }
    ]
}'
```

## OpenRouter Adapter

To try a real upstream provider, set `OPENROUTER_API_KEY` and run the OpenRouter example config:

```bash
OPENROUTER_API_KEY=... PYTHONPATH=src python -m agentforge_gateway.cli --config config.openrouter.example.json
```

Windows PowerShell:

```powershell
$env:OPENROUTER_API_KEY = "..."
$env:PYTHONPATH = "src"
python -m agentforge_gateway.cli --config config.openrouter.example.json
```

Then call the gateway with the local model alias:

```bash
curl http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openrouter-coder",
    "messages": [
      { "role": "user", "content": "Write a Python function." }
    ]
  }'
```
