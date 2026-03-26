from __future__ import annotations

import argparse


def retrieve(question: str) -> list[str]:
    # TODO 1: 根据问题返回最相关的知识片段
    raise NotImplementedError("请先完成 retrieve()。")


def answer(question: str) -> str:
    passages = retrieve(question)
    # TODO 2: 使用 passages 生成回答
    raise NotImplementedError(f"你已经拿到 {len(passages)} 个片段，继续完成 answer()。")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="starter 版本的 RAG agent。")
    parser.add_argument("--question", default="RAG 为什么要先检索？")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        print(answer(args.question))
    except NotImplementedError as error:
        print("starter 版本还没有完成。")
        print(error)


if __name__ == "__main__":
    main()
