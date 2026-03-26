from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os


def load_env_file(env_file: str) -> dict[str, str]:
    """读取最简单的 .env 文件，避免为入门项目引入额外依赖。"""
    env_path = Path(env_file)
    values: dict[str, str] = {}
    if not env_path.exists():
        return values

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


@dataclass
class AgentConfig:
    agent_name: str
    agent_style: str
    default_task: str

    @classmethod
    def load(cls, env_file: str = ".env") -> "AgentConfig":
        file_values = load_env_file(env_file)

        def read(key: str, default: str) -> str:
            return os.environ.get(key) or file_values.get(key) or default

        return cls(
            agent_name=read("AGENT_NAME", "AgentForge 小助手"),
            agent_style=read("AGENT_STYLE", "友好"),
            default_task=read("DEFAULT_TASK", "学习 Agent 基础"),
        )
