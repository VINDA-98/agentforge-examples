from __future__ import annotations

import argparse
from pathlib import Path

from team_orchestrator import MultiAgentTeam


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
    parser = argparse.ArgumentParser(description="运行一个最小多智能体协作项目。")
    parser.add_argument(
        "--brief",
        default="请为新手学员设计一次多智能体协作工作坊，本周五前交付活动方案",
        help="任务 brief",
    )
    parser.add_argument("--env-file", default=".env", help="配置文件路径")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    env_values = load_env_values(args.env_file)
    knowledge_path = env_values.get("TEAM_KNOWLEDGE_FILE", "data/team_knowledge.json")

    team = MultiAgentTeam(knowledge_path)
    result = team.collaborate(args.brief)

    print(f"协作状态：{result.status}")
    print("消息记录：")
    for index, message in enumerate(result.transcript, start=1):
        print(f"{index}. {message.sender} -> {message.recipient}：{message.content}")

    print()
    print("最终方案：")
    print(result.final_output)

    if result.review_notes:
        print()
        print("审阅建议：")
        for note in result.review_notes:
            print(f"- {note}")


if __name__ == "__main__":
    main()
