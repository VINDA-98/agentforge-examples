from __future__ import annotations

import argparse

from structured_output import (
    build_task_card,
    load_env_file,
    load_note_text,
    to_pretty_json,
    validate_task_card,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="运行一个最小结构化输出实验。")
    parser.add_argument("--input", default="data/sample_note.txt", help="原始笔记文件")
    parser.add_argument("--env-file", default=".env", help="配置文件路径")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    env_values = load_env_file(args.env_file)
    owner = env_values.get("DEFAULT_OWNER", "课程助教")

    note_text = load_note_text(args.input)
    payload = build_task_card(note_text, owner)
    is_valid, errors = validate_task_card(payload)

    print("结构化结果：")
    print(to_pretty_json(payload))
    print()
    print(f"校验结果：{'通过' if is_valid else '失败'}")
    if errors:
        for error in errors:
            print(f"- {error}")


if __name__ == "__main__":
    main()
