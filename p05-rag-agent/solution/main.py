from __future__ import annotations

import argparse


KNOWLEDGE = {
    "rag": "RAG 会先检索知识，再把相关内容交给生成步骤。",
    "tool": "Tool Calling 会先决定要不要调用工具。",
}


def retrieve(question: str) -> list[str]:
    normalized_question = question.lower()
    return [text for keyword, text in KNOWLEDGE.items() if keyword in normalized_question]


def answer(question: str) -> str:
    passages = retrieve(question)
    if not passages:
        return "没有找到相关知识。"
    return f"根据知识库：{passages[0]}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="solution 版本的 RAG agent。")
    parser.add_argument("--question", default="RAG 为什么要先检索？")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(answer(args.question))


if __name__ == "__main__":
    main()
