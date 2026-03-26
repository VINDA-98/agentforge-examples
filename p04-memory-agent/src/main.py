from __future__ import annotations

import argparse
from pathlib import Path

from memory_agent import MemoryAgent
from memory_store import ConversationMemory


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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="运行一个最小 memory-agent。")
    parser.add_argument("--session", default="demo", help="会话 ID")
    parser.add_argument("--message", default="你好", help="用户消息")
    parser.add_argument("--env-file", default=".env", help="配置文件路径")
    parser.add_argument("--reset", action="store_true", help="清空当前会话")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    env_values = load_env_values(args.env_file)
    memory_file = env_values.get("MEMORY_FILE", "data/memory_store.json")
    max_history = int(env_values.get("MAX_HISTORY", "6"))

    memory = ConversationMemory(memory_file=memory_file, max_history=max_history)
    if args.reset:
        memory.reset_session(args.session)
        print(f"已清空会话：{args.session}")
        return

    agent = MemoryAgent(memory)
    result = agent.handle_message(args.session, args.message)

    print(f"会话：{args.session}")
    print(f"已记录资料：{result.profile}")
    print(f"最近消息数：{result.history_count}")
    print(f"Agent 回复：{result.reply}")


if __name__ == "__main__":
    main()
