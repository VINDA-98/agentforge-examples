from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def load_note_text(input_path: str) -> str:
    return Path(input_path).read_text(encoding="utf-8").strip()


def build_task_card(note_text: str) -> dict[str, object]:
    action_items: list[str] = []
    for line in note_text.splitlines():
        match = re.match(r"^(?:[-*]|\d+[.)、])\s*(.+)$", line.strip())
        if match:
            action_items.append(match.group(1).strip())

    priority = "高" if "尽快" in note_text or "报错" in note_text else "中"
    return {
        "title": action_items[0] if action_items else "未命名任务",
        "summary": "这是 starter 的参考答案。",
        "action_items": action_items,
        "priority": priority,
        "owner": "课程助教",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="solution 版本的结构化输出实验。")
    parser.add_argument("--input", default="data/sample_note.txt")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    note_text = load_note_text(args.input)
    payload = build_task_card(note_text)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
