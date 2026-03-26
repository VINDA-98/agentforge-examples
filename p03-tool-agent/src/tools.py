from __future__ import annotations

from pathlib import Path
import json


def add_numbers(a: float, b: float) -> float:
    return a + b


def load_course_faq(faq_path: str) -> list[dict[str, object]]:
    return json.loads(Path(faq_path).read_text(encoding="utf-8"))


def lookup_course_answer(query: str, faq_path: str) -> str:
    normalized_query = query.lower()
    for record in load_course_faq(faq_path):
        keywords = [record["keyword"], *record.get("aliases", [])]
        if any(keyword.lower() in normalized_query for keyword in keywords):
            return str(record["answer"])
    return "暂时没有找到匹配的课程说明，请换一个更明确的关键词。"
