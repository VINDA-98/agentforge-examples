from __future__ import annotations

import argparse
import re


class ToolAgent:
    def choose_tool(self, query: str) -> str:
        if re.search(r"-?\d+(?:\.\d+)?\s*\+\s*-?\d+(?:\.\d+)?", query):
            return "calculator"
        return "course_lookup"

    def run(self, query: str) -> str:
        selected_tool = self.choose_tool(query)
        if selected_tool == "calculator":
            match = re.search(r"(-?\d+(?:\.\d+)?)\s*\+\s*(-?\d+(?:\.\d+)?)", query)
            if not match:
                return "没有找到可以计算的两个数字。"
            result = float(match.group(1)) + float(match.group(2))
            return f"我调用了 {selected_tool}，结果是 {result}。"
        return "我调用了 course_lookup，查到了 Tool Calling 的课程说明。"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="solution 版本的 tool-agent。")
    parser.add_argument("--query", default="什么是 Tool Calling")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    agent = ToolAgent()
    print(agent.run(args.query))


if __name__ == "__main__":
    main()
