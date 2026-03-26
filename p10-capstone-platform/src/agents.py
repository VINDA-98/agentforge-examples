from __future__ import annotations


class FaqAgent:
    def __init__(self, faq_items: list[dict[str, object]]):
        self.faq_items = faq_items

    def handle(self, message: str) -> str:
        for item in self.faq_items:
            keywords = [str(keyword) for keyword in item["keywords"]]
            if any(keyword in message for keyword in keywords):
                return str(item["answer"])
        return "还没有匹配到 FAQ，请补充更具体的问题。"


class PlanningAgent:
    def __init__(self, plan_templates: list[dict[str, object]]):
        self.plan_templates = plan_templates

    def handle(self, message: str) -> str:
        for template in self.plan_templates:
            keywords = [str(keyword) for keyword in template["keywords"]]
            if any(keyword in message for keyword in keywords):
                steps = [str(step) for step in template["steps"]]
                joined_steps = "；".join(f"{index}. {step}" for index, step in enumerate(steps, start=1))
                return f"建议分 {len(steps)} 步推进：{joined_steps}。"
        return "建议先明确目标用户、输入输出和验收标准，再决定平台模块。"


class DeliveryReviewAgent:
    def __init__(self, checklist: list[str]):
        self.checklist = checklist

    def handle(self, message: str) -> str:
        items = "；".join(f"{index}. {item}" for index, item in enumerate(self.checklist, start=1))
        return f"交付前请逐项检查：{items}。当前请求：{message}"
