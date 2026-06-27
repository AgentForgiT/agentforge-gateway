# API Contract

## Compatibility Target

Gateway v1 targets the OpenAI-compatible API shape used by common developer tools.

## Initial Endpoints

### `GET /v1/models`

Returns configured model aliases.

### `POST /v1/chat/completions`

Accepts chat completion requests and returns a normalized chat completion response.

## Later Endpoints

- `POST /v1/embeddings`
- `POST /v1/responses`
- `GET /health`
- `GET /metrics`

## Request Principles

- accept common OpenAI-compatible fields
- reject unsupported options clearly
- keep provider-specific options behind an explicit extension field
- do not silently ignore dangerous or unsupported behavior

## Response Principles

- return predictable error objects
- preserve provider request IDs when available
- normalize token usage when available
- mark estimated usage clearly when providers do not return exact usage
