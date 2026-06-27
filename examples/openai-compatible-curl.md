# OpenAI-Compatible Curl Example

Future local usage should look like this:

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Authorization: Bearer $AGENTFORGE_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "fast-coder",
    "messages": [
      {
        "role": "user",
        "content": "Write a Python function that validates an email address."
      }
    ]
  }'
```

