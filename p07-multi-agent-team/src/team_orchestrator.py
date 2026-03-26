from __future__ import annotations

from dataclasses import dataclass

from agents import AgentMessage, PlannerAgent, ResearcherAgent, ReviewerAgent, WriterAgent


@dataclass
class TeamResult:
    status: str
    transcript: list[AgentMessage]
    final_output: str
    review_notes: list[str]


class MultiAgentTeam:
    def __init__(self, knowledge_path: str):
        self.planner = PlannerAgent()
        self.researcher = ResearcherAgent(knowledge_path)
        self.writer = WriterAgent()
        self.reviewer = ReviewerAgent()

    def collaborate(self, brief: str) -> TeamResult:
        transcript = [AgentMessage("coordinator", "planner", brief)]

        plan = self.planner.respond(brief)
        transcript.append(
            AgentMessage(
                "planner",
                "coordinator",
                (
                    f"目标受众={plan['audience'] or '待补充'}；"
                    f"截止时间={plan['deadline'] or '待补充'}；"
                    f"任务数={len(plan['tasks'])}"
                ),
            )
        )

        research_notes = self.researcher.respond(brief)
        transcript.append(
            AgentMessage(
                "researcher",
                "coordinator",
                "；".join(research_notes),
            )
        )

        draft = self.writer.respond(brief, plan, research_notes)
        transcript.append(
            AgentMessage("writer", "coordinator", "已生成活动方案草稿。")
        )

        review_result = self.reviewer.respond(draft, plan)
        transcript.append(
            AgentMessage("reviewer", "coordinator", str(review_result["message"]))
        )

        status = "ready" if review_result["approved"] else "needs_revision"
        return TeamResult(
            status=status,
            transcript=transcript,
            final_output=draft,
            review_notes=[str(item) for item in review_result["issues"]],
        )
