from __future__ import annotations

from dataclasses import dataclass
import re

from tools import add_numbers, lookup_course_answer


@dataclass
class AgentRunResult:
    selected_tool: str
    tool_input: dict[str, object]
    tool_output: object
    final_answer: str


class ToolAgent:
    def __init__(self, faq_path: str):
        self.faq_path = faq_path

    def choose_tool(self, query: str) -> str:
        if re.search(r"-?\d+(?:\.\d+)?\s*\+\s*-?\d+(?:\.\d+)?", query):
            return "calculator"
        if "加" in query or "求和" in query or "总和" in query:
            return "calculator"
        return "course_lookup"

    def extract_numbers(self, query: str) -> tuple[float, float]:
        match = re.search(r"(-?\d+(?:\.\d+)?)\s*\+\s*(-?\d+(?:\.\d+)?)", query)
        if match:
            return float(match.group(1)), float(match.group(2))

        numbers = re.findall(r"-?\d+(?:\.\d+)?", query)
        if len(numbers) >= 2:
            return float(numbers[0]), float(numbers[1])
        raise ValueError("没有从问题里找到两个可相加的数字。")

    def run(self, query: str) -> AgentRunResult:
        selected_tool = self.choose_tool(query)

        if selected_tool == "calculator":
            a, b = self.extract_numbers(query)
            output = add_numbers(a, b)
            return AgentRunResult(
                selected_tool=selected_tool,
                tool_input={"a": a, "b": b},
                tool_output=output,
                final_answer=f"我调用了 {selected_tool}，计算结果是 {output}。",
            )

        answer = lookup_course_answer(query, self.faq_path)
        return AgentRunResult(
            selected_tool=selected_tool,
            tool_input={"query": query},
            tool_output=answer,
            final_answer=f"我调用了 {selected_tool}，查询结果是：{answer}",
        )
