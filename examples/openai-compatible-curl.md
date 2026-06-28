# OpenAI-Compatible Curl Examples

Mock provider:

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mock-coder",
    "messages": [
      {
        "role": "user",
        "content": "Write a Python function that validates an email address."
      }
    ]
}'
```

OpenRouter provider:

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openrouter-coder",
    "messages": [
      {
        "role": "user",
        "content": "Write a Python function that validates an email address."
      }
    ]
  }'
```
