from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


AUDIENCE_KEYWORDS = ["新手学员", "新手", "学员", "企业客户", "内部团队"]
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


@dataclass
class AgentMessage:
    sender: str
    recipient: str
    content: str


def detect_audience(brief: str) -> str | None:
    for keyword in AUDIENCE_KEYWORDS:
        if keyword in brief:
            return keyword
    return None


def detect_deadline(brief: str) -> str | None:
    for keyword in DEADLINE_HINTS:
        if keyword in brief:
            return keyword
    return None


def detect_topic(brief: str) -> str:
    if "直播" in brief:
        return "直播活动"
    if "工作坊" in brief:
        return "多智能体协作工作坊"
    if "训练营" in brief:
        return "训练营活动"
    return "课程协作活动"


def load_knowledge_cards(knowledge_path: str) -> list[dict[str, str]]:
    return json.loads(Path(knowledge_path).read_text(encoding="utf-8"))


class PlannerAgent:
    def respond(self, brief: str) -> dict[str, object]:
        audience = detect_audience(brief)
        deadline = detect_deadline(brief)
        topic = detect_topic(brief)

        tasks = [
            "明确活动目标和交付物",
            "拆分讲解、演示和互动环节",
            "安排宣传、执行和复盘负责人",
            "确认活动前后的沟通节奏",
        ]
        if deadline:
            tasks.append(f"在 {deadline} 前完成内部确认")

        return {
            "topic": topic,
            "audience": audience,
            "deadline": deadline,
            "deliverables": ["活动方案", "宣传文案", "复盘记录"],
            "tasks": tasks,
        }


class ResearcherAgent:
    def __init__(self, knowledge_path: str):
        self.knowledge_cards = load_knowledge_cards(knowledge_path)

    def respond(self, brief: str) -> list[str]:
        matched_cards = [
            card["advice"]
            for card in self.knowledge_cards
            if card["tag"] in brief
        ]
        if not matched_cards:
            matched_cards.append("默认建议：方案里至少写清主题、时间线、交付物和验收方式。")
        return matched_cards


class WriterAgent:
    def respond(
        self, brief: str, plan: dict[str, object], research_notes: list[str]
    ) -> str:
        audience = plan["audience"] or "待补充"
        deadline = plan["deadline"] or "待补充"
        tasks = "\n".join(f"- {item}" for item in plan["tasks"])
        notes = "\n".join(f"- {item}" for item in research_notes)
        deliverables = "、".join(str(item) for item in plan["deliverables"])

        return (
            f"项目主题：{plan['topic']}\n"
            f"项目背景：{brief}\n"
            f"目标受众：{audience}\n"
            f"时间线：{deadline}\n"
            f"交付物：{deliverables}\n"
            "执行拆分：\n"
            f"{tasks}\n"
            "调研补充：\n"
            f"{notes}"
        )


class ReviewerAgent:
    def respond(self, draft: str, plan: dict[str, object]) -> dict[str, object]:
        issues: list[str] = []
        if plan["deadline"] is None:
            issues.append("缺少明确截止时间。")
        if plan["audience"] is None:
            issues.append("缺少明确目标受众。")
        if "交付物：" not in draft:
            issues.append("草稿里没有写出交付物。")

        if issues:
            return {
                "approved": False,
                "message": "草稿需要修改后再执行。",
                "issues": issues,
            }

        return {
            "approved": True,
            "message": "草稿通过，可以进入执行。",
            "issues": [],
        }
