from __future__ import annotations

import argparse
from pathlib import Path

from tool_agent import ToolAgent


def load_env_value(env_file: str, key: str, default: str) -> str:
    env_path = Path(env_file)
    if not env_path.exists():
        return default

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        current_key, value = line.split("=", 1)
        if current_key.strip() == key:
            return value.strip()
    return default


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="运行一个最小 tool-agent。")
    parser.add_argument("--query", default="什么是 Tool Calling", help="用户问题")
    parser.add_argument("--env-file", default=".env", help="配置文件路径")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    faq_path = load_env_value(args.env_file, "FAQ_FILE", "data/course_faq.json")
    agent = ToolAgent(faq_path=faq_path)
    result = agent.run(args.query)

    print(f"选择工具：{result.selected_tool}")
    print(f"工具输入：{result.tool_input}")
    print(f"工具结果：{result.tool_output}")
    print(f"最终回答：{result.final_answer}")


if __name__ == "__main__":
    main()
