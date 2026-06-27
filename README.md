# agentforge-gateway

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
