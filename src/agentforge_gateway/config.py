from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ModelConfig:
    name: str
    provider: str
    provider_model: str


@dataclass(frozen=True)
class GatewayConfig:
    host: str
    port: int
    models: dict[str, ModelConfig]


DEFAULT_CONFIG = GatewayConfig(
    host="127.0.0.1",
    port=8080,
    models={
        "mock-coder": ModelConfig(
            name="mock-coder",
            provider="mock",
            provider_model="mock-coder-v1",
        )
    },
)


def load_config(path: str | Path | None = None) -> GatewayConfig:
    if path is None:
        return DEFAULT_CONFIG

    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    return parse_config(raw)


def parse_config(raw: dict[str, Any]) -> GatewayConfig:
    server = raw.get("server", {})
    models = raw.get("models", {})

    if not isinstance(models, dict) or not models:
        raise ValueError("config must define at least one model")

    parsed_models: dict[str, ModelConfig] = {}
    for name, model in models.items():
        if not isinstance(model, dict):
            raise ValueError(f"model '{name}' must be an object")
        provider = model.get("provider")
        provider_model = model.get("provider_model")
        if not provider or not provider_model:
            raise ValueError(f"model '{name}' requires provider and provider_model")
        parsed_models[name] = ModelConfig(
            name=name,
            provider=str(provider),
            provider_model=str(provider_model),
        )

    return GatewayConfig(
        host=str(server.get("host", "127.0.0.1")),
        port=int(server.get("port", 8080)),
        models=parsed_models,
    )

