from __future__ import annotations

import argparse


def analyze_code(request: str) -> str:
    if "删除整个项目" in request or "rm -rf" in request:
        return "护栏已拦截：禁止破坏性请求。"
    return "建议先检查调试输出、除零保护和异常处理。"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="solution 版本的编码智能体实验项目。")
    parser.add_argument("--request", default="请检查这个 Python 文件里的问题")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(analyze_code(args.request))


if __name__ == "__main__":
    main()
