# OpenAI-Compatible Curl Example

Future local usage should look like this:

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
