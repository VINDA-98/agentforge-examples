from __future__ import annotations

import argparse

from config import AgentConfig
from hello_agent import HelloAgent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="运行一个最小 hello-agent。")
    parser.add_argument("--name", default="同学", help="用户姓名")
    parser.add_argument("--task", default="", help="当前任务")
    parser.add_argument("--env-file", default=".env", help="配置文件路径")
    parser.add_argument("--show-prompt", action="store_true", help="额外打印内部提示词")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    config = AgentConfig.load(args.env_file)
    agent = HelloAgent(config)
    result = agent.run(user_name=args.name, task=args.task)

    print(f"Agent 名称：{config.agent_name}")
    print(f"用户：{args.name}")
    print(f"任务：{args.task or config.default_task}")
    print()
    if args.show_prompt:
        print("内部提示词：")
        print(result.prompt)
        print()
    print(result.response)


if __name__ == "__main__":
    main()
