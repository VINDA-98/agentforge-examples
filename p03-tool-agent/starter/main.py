from __future__ import annotations

import argparse


class ToolAgent:
    def choose_tool(self, query: str) -> str:
        # TODO 1: 根据 query 判断应该用 calculator 还是 course_lookup
        raise NotImplementedError("请先完成 choose_tool()。")

    def run(self, query: str) -> str:
        selected_tool = self.choose_tool(query)
        # TODO 2: 调用工具后，把结果拼成一段文字
        raise NotImplementedError(f"你已经选中了工具：{selected_tool}，继续完成 run()。")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="starter 版本的 tool-agent。")
    parser.add_argument("--query", default="什么是 Tool Calling")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    agent = ToolAgent()
    try:
        print(agent.run(args.query))
    except NotImplementedError as error:
        print("starter 版本还没有完成。")
        print(error)


if __name__ == "__main__":
    main()
