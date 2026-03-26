from __future__ import annotations

import argparse
import re


class MemoryAgent:
    def extract_profile_updates(self, message: str) -> dict[str, str]:
        profile: dict[str, str] = {}
        name_match = re.search(r"(?:我叫|我的名字是)(?!什么)([\u4e00-\u9fa5A-Za-z0-9_-]+)", message)
        if name_match:
            profile["name"] = name_match.group(1)

        goal_match = re.search(r"(?:我想学|我正在学)(.+)", message)
        if goal_match:
            profile["goal"] = goal_match.group(1).strip("。！!？? ")
        return profile

    def build_reply(self, message: str, profile: dict[str, str]) -> str:
        if "name" in profile:
            return f"记住了，你叫{profile['name']}。"
        if "goal" in profile:
            return f"记住了，你想学 {profile['goal']}。"
        return f"我记录了这条消息：{message}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="solution 版本的 memory-agent。")
    parser.add_argument("--message", default="我叫小王")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    agent = MemoryAgent()
    profile = agent.extract_profile_updates(args.message)
    print(agent.build_reply(args.message, profile))


if __name__ == "__main__":
    main()
