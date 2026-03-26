from __future__ import annotations

import json
from pathlib import Path


TASK_TYPE_RULES = {
    "live_event": ["直播", "分享会", "公开课"],
    "course_launch": ["发布", "上线", "课程"],
    "incident_response": ["修复", "故障", "问题", "报警"],
}

AUDIENCE_KEYWORDS = ["新手学员", "新手", "学员", "讲师", "内部团队", "企业客户"]
DEADLINE_HINTS = [
    "本周一",
    "本周二",
    "本周三",
    "本周四",
    "本周五",
    "本周六",
    "本周日",
    "下周一",
    "下周二",
    "下周三",
    "下周四",
    "下周五",
    "下周六",
    "下周日",
    "今天",
    "明天",
    "周一",
    "周二",
    "周三",
    "周四",
    "周五",
    "周六",
    "周日",
    "本周",
    "下周",
]
RISK_KEYWORDS = {
    "生产环境": "涉及生产环境操作",
    "删除": "涉及删除动作",
    "付款": "涉及资金或付款动作",
    "对外承诺": "涉及对外承诺",
}


def load_templates(template_path: str) -> dict[str, dict[str, object]]:
    return json.loads(Path(template_path).read_text(encoding="utf-8"))


def detect_task_type(request: str, templates: dict[str, dict[str, object]]) -> tuple[str, str]:
    for task_type, keywords in TASK_TYPE_RULES.items():
        if any(keyword in request for keyword in keywords):
            return task_type, str(templates[task_type]["label"])
    generic_template = templates["generic_task"]
    return "generic_task", str(generic_template["label"])


def detect_audience(request: str) -> str | None:
    for keyword in AUDIENCE_KEYWORDS:
        if keyword in request:
            return keyword
    return None


def detect_deadline(request: str) -> str | None:
    for keyword in DEADLINE_HINTS:
        if keyword in request:
            return keyword
    return None


def analyze_request(
    request: str, templates: dict[str, dict[str, object]]
) -> dict[str, object]:
    task_type, task_label = detect_task_type(request, templates)
    audience = detect_audience(request)
    deadline = detect_deadline(request)

    missing_fields: list[str] = []
    if audience is None:
        missing_fields.append("目标人群")
    if deadline is None:
        missing_fields.append("截止时间")

    return {
        "task_type": task_type,
        "task_label": task_label,
        "audience": audience,
        "deadline": deadline,
        "missing_fields": missing_fields,
    }


def build_plan(context: dict[str, object], templates: dict[str, dict[str, object]]) -> list[str]:
    template = templates[str(context["task_type"])]
    tasks = [str(item) for item in template["tasks"]]

    if context["audience"]:
        tasks[0] = f"{tasks[0]}，重点服务 {context['audience']}"
    if context["deadline"]:
        tasks.append(f"在 {context['deadline']} 前完成一次结果复核")
    return tasks


def assess_risk(request: str) -> list[str]:
    matched_risks = []
    for keyword, description in RISK_KEYWORDS.items():
        if keyword in request:
            matched_risks.append(description)
    return matched_risks
