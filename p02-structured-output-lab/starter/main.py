from __future__ import annotations

import argparse
from pathlib import Path


def load_note_text(input_path: str) -> str:
    return Path(input_path).read_text(encoding="utf-8").strip()


def build_task_card(note_text: str) -> dict[str, object]:
    # TODO 1: 提取标题
    # TODO 2: 提取 action_items 列表
    # TODO 3: 根据关键词判断 priority
    raise NotImplementedError("请先补全 build_task_card()。")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="starter 版本的结构化输出实验。")
    parser.add_argument("--input", default="data/sample_note.txt")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    note_text = load_note_text(args.input)
    try:
        print(build_task_card(note_text))
    except NotImplementedError as error:
        print("starter 版本还没有完成。")
        print(error)


if __name__ == "__main__":
    main()
