from __future__ import annotations

import argparse


class MemoryAgent:
    def extract_profile_updates(self, message: str) -> dict[str, str]:
        # TODO 1: 从消息中提取 name / goal
        raise NotImplementedError("请先完成 extract_profile_updates()。")

    def build_reply(self, message: str, profile: dict[str, str]) -> str:
        # TODO 2: 根据 profile 生成回复
        raise NotImplementedError("请先完成 build_reply()。")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="starter 版本的 memory-agent。")
    parser.add_argument("--message", default="我叫小王")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    agent = MemoryAgent()
    try:
        profile = agent.extract_profile_updates(args.message)
        print(agent.build_reply(args.message, profile))
    except NotImplementedError as error:
        print("starter 版本还没有完成。")
        print(error)


if __name__ == "__main__":
    main()
