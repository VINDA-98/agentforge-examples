from __future__ import annotations

import argparse


def analyze_code(request: str, file_path: str) -> list[str]:
    # TODO 1: 读取 file_path，并返回问题列表
    raise NotImplementedError("请先完成 analyze_code()。")


def run_eval() -> str:
    # TODO 2: 运行最小评测，并返回总结
    raise NotImplementedError("请先完成 run_eval()。")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="starter 版本的编码智能体实验项目。")
    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze_parser = subparsers.add_parser("analyze")
    analyze_parser.add_argument("--file", default="data/sample_buggy_module.py")
    analyze_parser.add_argument("--request", default="请检查这个 Python 文件里的问题")

    subparsers.add_parser("eval")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        if args.command == "analyze":
            print(analyze_code(args.request, args.file))
        else:
            print(run_eval())
    except NotImplementedError as error:
        print("starter 版本还没有完成。")
        print(error)


if __name__ == "__main__":
    main()
