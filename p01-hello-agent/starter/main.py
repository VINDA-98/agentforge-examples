from __future__ import annotations

import argparse


class HelloAgent:
    def build_response(self, user_name: str, task: str) -> str:
        # TODO 1: 把 user_name 和 task 组合成一段完整回复。
        # 目标效果可以参考 README 或 solution/main.py。
        raise NotImplementedError("请先完成 build_response() 中的 TODO。")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="starter 版本的 hello-agent。")
    parser.add_argument("--name", default="同学")
    parser.add_argument("--task", default="学习 Agent 基础")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    agent = HelloAgent()
    try:
        print(agent.build_response(args.name, args.task))
    except NotImplementedError as error:
        print("starter 版本还没有完成。")
        print(error)


if __name__ == "__main__":
    main()
