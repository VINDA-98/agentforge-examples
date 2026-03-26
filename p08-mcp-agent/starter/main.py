from __future__ import annotations

import argparse


def discover_tools(server_name: str) -> list[str]:
    # TODO 1: 返回某个 server 的工具列表
    raise NotImplementedError("请先完成 discover_tools()。")


def call_tool(server_name: str, tool_name: str, arguments: dict[str, str]) -> object:
    # TODO 2: 执行工具调用
    raise NotImplementedError("请先完成 call_tool()。")


def answer_question(question: str) -> str:
    # TODO 3: 根据问题决定 server 和 tool，并返回最终回答
    raise NotImplementedError("请先完成 answer_question()。")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="starter 版本的 MCP 风格接入项目。")
    parser.add_argument("--question", default="p08 项目现在是什么状态？")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        print(answer_question(args.question))
    except NotImplementedError as error:
        print("starter 版本还没有完成。")
        print(error)


if __name__ == "__main__":
    main()
