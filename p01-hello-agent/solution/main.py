from __future__ import annotations

import argparse


class HelloAgent:
    def build_response(self, user_name: str, task: str) -> str:
        return "\n".join(
            [
                f"你好，{user_name}！",
                "我是 starter 的参考实现版本。",
                f"我收到的任务是：{task}。",
                "你已经完成了最小 Agent 的核心拼装。",
            ]
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="solution 版本的 hello-agent。")
    parser.add_argument("--name", default="同学")
    parser.add_argument("--task", default="学习 Agent 基础")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    agent = HelloAgent()
    print(agent.build_response(args.name, args.task))


if __name__ == "__main__":
    main()
