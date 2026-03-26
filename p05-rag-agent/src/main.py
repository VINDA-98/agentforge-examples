from __future__ import annotations

import argparse
from pathlib import Path

from rag_agent import RagAgent


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
    parser = argparse.ArgumentParser(description="运行一个最小 RAG agent。")
    parser.add_argument("--question", default="RAG 为什么要先检索？", help="用户问题")
    parser.add_argument("--env-file", default=".env", help="配置文件路径")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    env_values = load_env_values(args.env_file)
    knowledge_path = env_values.get("KNOWLEDGE_FILE", "data/knowledge_base.json")
    top_k = int(env_values.get("TOP_K", "2"))

    agent = RagAgent(knowledge_path=knowledge_path, top_k=top_k)
    result = agent.answer(args.question)

    if result.passages:
        print("命中片段：")
        for index, passage in enumerate(result.passages, start=1):
            print(f"{index}. [{passage['source']}] {passage['text']}")
        print()
    else:
        print("命中片段：无")
        print()

    print(f"最终回答：{result.answer}")


if __name__ == "__main__":
    main()
