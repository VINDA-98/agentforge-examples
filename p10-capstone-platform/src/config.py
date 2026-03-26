from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class PlatformConfig:
    data_file: str
    host: str
    port: int


def load_env_values(env_file: str) -> dict[str, str]:
    values: dict[str, str] = {}
    env_path = Path(env_file)
    if not env_path.exists():
        return values

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def load_config(env_file: str) -> PlatformConfig:
    env_values = load_env_values(env_file)
    return PlatformConfig(
        data_file=env_values.get("PLATFORM_DATA_FILE", "data/platform_catalog.json"),
        host=env_values.get("PLATFORM_HOST", "127.0.0.1"),
        port=int(env_values.get("PLATFORM_PORT", "8787")),
    )
