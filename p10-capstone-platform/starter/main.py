from __future__ import annotations

import argparse


def select_agent(request_type: str):
    # TODO 1: 根据 request_type 返回对应的处理函数
    raise NotImplementedError("请先完成 select_agent()。")


def handle_request(request_type: str, message: str) -> str:
    # TODO 2: 调用 select_agent() 并返回处理结果
    raise NotImplementedError("请先完成 handle_request()。")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="starter 版本的毕业项目平台。")
    parser.add_argument("--request-type", default="faq")
    parser.add_argument("--message", default="p10 项目适用于哪些章节？")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        print(handle_request(args.request_type, args.message))
    except NotImplementedError as error:
        print("starter 版本还没有完成。")
        print(error)


if __name__ == "__main__":
    main()
