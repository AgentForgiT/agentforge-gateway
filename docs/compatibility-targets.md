# Compatibility Targets

## V1 Client Targets

Gateway v1 should work with tools that can call an OpenAI-compatible base URL.

Initial target categories:

- IDE assistants
- coding agent CLIs
- local scripts
- benchmark runners
- documentation examples

## Specific Tools To Test

- VS Code extensions that accept OpenAI-compatible endpoints
- Continue
- Roo Code
- Cline
- Aider
- Codex CLI
- Claude Code when compatible routing is available
- local curl and Python clients

## Compatibility Notes

Different tools vary in how strictly they expect OpenAI responses. Gateway compatibility should be tested per tool and documented with exact configuration examples.

## Acceptance Criteria

For each supported tool, document:

- required base URL
- auth header behavior
- model name configuration
- streaming support
- known limitations
