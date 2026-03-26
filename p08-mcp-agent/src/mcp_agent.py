from __future__ import annotations

from dataclasses import dataclass
import re

from mock_mcp_server import MockMcpClient


@dataclass
class McpAgentResult:
    server_name: str
    tools: list[str]
    selected_tool: str
    arguments: dict[str, str]
    tool_result: object
    answer: str


def choose_server(question: str) -> str:
    if "规范" in question or "starter" in question or "中文" in question:
        return "course_policy"
    return "course_ops"


def choose_tool(server_name: str, question: str) -> tuple[str, dict[str, str]]:
    if server_name == "course_policy":
        keyword = "starter"
        if "中文" in question:
            keyword = "中文"
        if "测试" in question:
            keyword = "测试"
        return "search_policy", {"keyword": keyword}

    if "工作坊" in question or "活动" in question:
        return "list_workshops", {}

    match = re.search(r"p\d{2}", question.lower())
    if match:
        return "get_project_status", {"project_key": match.group(0)}
    return "list_workshops", {}


def format_answer(tool_name: str, tool_result: object) -> str:
    if tool_name == "get_project_status":
        payload = dict(tool_result)
        return (
            f"项目 {payload['project_key']} 当前状态是{payload['status']}，"
            f"负责人是 {payload['owner']}，下一步是{payload['next_step']}。"
        )

    if tool_name == "list_workshops":
        workshops = [
            f"{item['title']}（{item['time']}）"
            for item in tool_result
        ]
        return f"本周工作坊包括：{'、'.join(workshops)}。"

    if tool_name == "search_policy":
        first_match = tool_result[0]
        return f"查询到的规范：{first_match['content']}"

    return "工具调用完成。"


class McpAgent:
    def __init__(self, data_path: str):
        self.client = MockMcpClient(data_path)

    def answer_question(self, question: str) -> McpAgentResult:
        server_name = choose_server(question)
        session = self.client.connect(server_name)
        tools = session.list_tools()
        selected_tool, arguments = choose_tool(server_name, question)
        tool_result = session.call_tool(selected_tool, arguments)
        answer = format_answer(selected_tool, tool_result)
        return McpAgentResult(
            server_name=server_name,
            tools=[tool.name for tool in tools],
            selected_tool=selected_tool,
            arguments=arguments,
            tool_result=tool_result,
            answer=answer,
        )
