from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import uuid

from agents import DeliveryReviewAgent, FaqAgent, PlanningAgent


@dataclass
class RunResult:
    run_id: str
    status: str
    agent: str
    output: str


class PlatformService:
    def __init__(self, data_file: str):
        catalog = json.loads(Path(data_file).read_text(encoding="utf-8"))
        self.agent_descriptions = {
            "faq": "回答课程和项目常见问题",
            "plan": "根据需求生成最小落地计划",
            "review": "根据检查清单做交付检查",
        }
        self.agents = {
            "faq": FaqAgent(list(catalog["faq"])),
            "plan": PlanningAgent(list(catalog["plan_templates"])),
            "review": DeliveryReviewAgent(list(catalog["review_checklist"])),
        }

    def health(self) -> dict[str, object]:
        return {
            "status": "ok",
            "agent_count": len(self.agents),
        }

    def list_agents(self) -> list[dict[str, str]]:
        return [
            {"type": agent_type, "description": description}
            for agent_type, description in self.agent_descriptions.items()
        ]

    def handle_request(self, request_type: str, message: str) -> dict[str, str]:
        if request_type not in self.agents:
            raise ValueError(f"不支持的请求类型：{request_type}")
        if not message.strip():
            raise ValueError("message 不能为空。")

        output = self.agents[request_type].handle(message)
        result = RunResult(
            run_id=f"run-{uuid.uuid4().hex[:8]}",
            status="completed",
            agent=request_type,
            output=output,
        )
        return {
            "run_id": result.run_id,
            "status": result.status,
            "agent": result.agent,
            "output": result.output,
        }
