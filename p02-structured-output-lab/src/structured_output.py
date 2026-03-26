from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import json
import re


def load_env_file(env_file: str) -> dict[str, str]:
    values: dict[str, str] = {}
    env_path = Path(env_file)
    if not env_path.exists():
        return values

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def load_note_text(input_path: str) -> str:
    return Path(input_path).read_text(encoding="utf-8").strip()


@dataclass
class TaskCard:
    title: str
    summary: str
    action_items: list[str]
    priority: str
    owner: str


def extract_action_items(note_text: str) -> list[str]:
    items: list[str] = []
    pattern = re.compile(r"^(?:[-*]|\d+[.)、])\s*(.+)$")
    for line in note_text.splitlines():
        match = pattern.match(line.strip())
        if match:
            items.append(match.group(1).strip())
    return items


def guess_title(note_text: str, action_items: list[str]) -> str:
    if action_items:
        return action_items[0]

    for line in note_text.splitlines():
        cleaned = line.strip()
        if cleaned:
            return cleaned[:20]
    return "未命名任务"


def guess_priority(note_text: str) -> str:
    high_keywords = ("今天", "尽快", "马上", "bug", "报错")
    medium_keywords = ("本周", "安排", "整理")

    if any(keyword in note_text for keyword in high_keywords):
        return "高"
    if any(keyword in note_text for keyword in medium_keywords):
        return "中"
    return "低"


def build_task_card(note_text: str, owner: str) -> dict[str, object]:
    action_items = extract_action_items(note_text)
    card = TaskCard(
        title=guess_title(note_text, action_items),
        summary="从原始笔记中整理出一张最小任务卡片。",
        action_items=action_items,
        priority=guess_priority(note_text),
        owner=owner,
    )
    return asdict(card)


def validate_task_card(payload: dict[str, object]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    required_fields = {
        "title": str,
        "summary": str,
        "action_items": list,
        "priority": str,
        "owner": str,
    }

    for field_name, expected_type in required_fields.items():
        if field_name not in payload:
            errors.append(f"缺少字段：{field_name}")
            continue
        if not isinstance(payload[field_name], expected_type):
            errors.append(f"字段 {field_name} 的类型应为 {expected_type.__name__}")

    action_items = payload.get("action_items", [])
    if isinstance(action_items, list) and not action_items:
        errors.append("action_items 不能为空")

    priority = payload.get("priority")
    if isinstance(priority, str) and priority not in {"高", "中", "低"}:
        errors.append("priority 只能是 高 / 中 / 低")

    return not errors, errors


def to_pretty_json(payload: dict[str, object]) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2)
