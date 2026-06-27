from __future__ import annotations

from http.server import ThreadingHTTPServer
import json
import sys
from pathlib import Path
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from agentforge_gateway.app import GatewayApp, create_handler
from agentforge_gateway.config import DEFAULT_CONFIG


class GatewayAppTests(unittest.TestCase):
    def setUp(self) -> None:
        self.app = GatewayApp(DEFAULT_CONFIG)

    def test_health(self) -> None:
        self.assertEqual(self.app.health()["status"], "ok")

    def test_models(self) -> None:
        models = self.app.models()
        self.assertEqual(models["object"], "list")
        self.assertEqual(models["data"][0]["id"], "mock-coder")

    def test_chat_completion(self) -> None:
        response = self.app.chat_completions(
            {
                "model": "mock-coder",
                "messages": [{"role": "user", "content": "Hello"}],
            }
        )

        self.assertEqual(response["object"], "chat.completion")
        self.assertEqual(response["model"], "mock-coder")
        self.assertIn("Mock response", response["choices"][0]["message"]["content"])

    def test_unknown_model(self) -> None:
        with self.assertRaises(Exception) as ctx:
            self.app.chat_completions(
                {
                    "model": "missing",
                    "messages": [{"role": "user", "content": "Hello"}],
                }
            )

        self.assertIn("unknown model", str(ctx.exception))

    def test_malformed_request(self) -> None:
        with self.assertRaises(Exception) as ctx:
            self.app.chat_completions({"model": "mock-coder"})

        self.assertIn("messages", str(ctx.exception))


class GatewayHttpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        app = GatewayApp(DEFAULT_CONFIG)
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), create_handler(app))
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        host, port = cls.server.server_address
        cls.base_url = f"http://{host}:{port}"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=5)

    def test_health_endpoint(self) -> None:
        body = self.get_json("/health")
        self.assertEqual(body["status"], "ok")

    def test_models_endpoint(self) -> None:
        body = self.get_json("/v1/models")
        self.assertEqual(body["data"][0]["id"], "mock-coder")

    def test_chat_completions_endpoint(self) -> None:
        body = self.post_json(
            "/v1/chat/completions",
            {
                "model": "mock-coder",
                "messages": [{"role": "user", "content": "Write a test."}],
            },
        )
        self.assertEqual(body["choices"][0]["message"]["role"], "assistant")

    def test_unknown_model_endpoint(self) -> None:
        with self.assertRaises(HTTPError) as ctx:
            self.post_json(
                "/v1/chat/completions",
                {
                    "model": "missing",
                    "messages": [{"role": "user", "content": "Hello"}],
                },
            )

        self.assertEqual(ctx.exception.code, 404)

    def get_json(self, path: str) -> dict[str, object]:
        with urlopen(f"{self.base_url}{path}") as response:
            return json.loads(response.read().decode("utf-8"))

    def post_json(self, path: str, body: dict[str, object]) -> dict[str, object]:
        request = Request(
            f"{self.base_url}{path}",
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request) as response:
            return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    unittest.main()

