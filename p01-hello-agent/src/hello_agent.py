from __future__ import annotations

from dataclasses import dataclass

from config import AgentConfig


@dataclass
class AgentResult:
    prompt: str
    response: str


class HelloAgent:
    """一个最小 Agent，用固定规则模拟一次“收到任务后给出回应”的过程。"""

    def __init__(self, config: AgentConfig):
        self.config = config

    def build_prompt(self, user_name: str, task: str) -> str:
        return (
            f"你是 {self.config.agent_name}，"
            f"请用{self.config.agent_style}的方式回答用户。"
            f"用户叫 {user_name}，当前目标是：{task}。"
        )

    def build_response(self, user_name: str, task: str) -> str:
        return "\n".join(
            [
                f"你好，{user_name}！",
                f"我是 {self.config.agent_name}，会用{self.config.agent_style}的方式解释 Agent 项目。",
                f"我收到的当前目标是：{task}。",
                "建议先完成三步：读取输入、组合提示词、输出稳定结果。",
            ]
        )

    def run(self, user_name: str, task: str) -> AgentResult:
        normalized_user = user_name.strip() or "同学"
        normalized_task = task.strip() or self.config.default_task
        return AgentResult(
            prompt=self.build_prompt(normalized_user, normalized_task),
            response=self.build_response(normalized_user, normalized_task),
        )
