# Roadmap

## Phase 0: Design Baseline

- define Gateway v1 scope
- document OpenAI-compatible API surface
- document provider routing strategy
- document key management strategy
- define compatibility targets

## Phase 1: Local MVP

- create minimal HTTP service
- implement `/v1/models`
- implement `/v1/chat/completions`
- add one mock provider adapter
- add basic request validation
- add one real provider adapter

## Phase 2: Provider Layer

- add provider registry
- add route selection rules
- add provider health checks
- add timeout and retry policy
- add local provider support

## Phase 3: Developer Experience

- add Docker Compose
- add `.env.example`
- add examples for common clients
- add compatibility notes for agentic IDEs and CLIs
- add CI validation

## Phase 4: Observability and Hardening

- add structured logs
- add metrics
- add request tracing hooks
- add redaction rules
- add security review checklist
