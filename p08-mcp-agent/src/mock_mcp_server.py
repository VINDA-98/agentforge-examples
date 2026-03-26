from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path


def load_mcp_definition(data_path: str) -> dict[str, object]:
    return json.loads(Path(data_path).read_text(encoding="utf-8"))


@dataclass
class McpTool:
    name: str
    description: str
    input_schema: dict[str, str]


class MockMcpSession:
    def __init__(self, server_definition: dict[str, object], datasets: dict[str, object]):
        self.server_definition = server_definition
        self.datasets = datasets

    def list_tools(self) -> list[McpTool]:
        return [
            McpTool(
                name=str(tool["name"]),
                description=str(tool["description"]),
                input_schema={str(key): str(value) for key, value in tool["input_schema"].items()},
            )
            for tool in self.server_definition["tools"]
        ]

    def call_tool(self, tool_name: str, arguments: dict[str, str]) -> object:
        if tool_name == "get_project_status":
            project_key = arguments.get("project_key", "").lower()
            project_status = self.datasets["project_status"]
            if project_key not in project_status:
                raise ValueError(f"没有找到项目：{project_key}")
            payload = dict(project_status[project_key])
            payload["project_key"] = project_key
            return payload

        if tool_name == "list_workshops":
            return list(self.datasets["workshops"])

        if tool_name == "search_policy":
            keyword = arguments.get("keyword", "").lower()
            matches = [
                policy
                for policy in self.datasets["policies"]
                if keyword and keyword in str(policy["keyword"]).lower()
            ]
            if not matches:
                return [{"keyword": keyword, "content": "没有找到对应规范，请换个关键词。"}]
            return matches

        raise ValueError(f"当前 server 不支持工具：{tool_name}")


class MockMcpClient:
    def __init__(self, data_path: str):
        definition = load_mcp_definition(data_path)
        self.datasets = dict(definition["datasets"])
        self.servers = {
            str(server["name"]): server
            for server in definition["servers"]
        }

    def connect(self, server_name: str) -> MockMcpSession:
        if server_name not in self.servers:
            raise ValueError(f"没有找到 server：{server_name}")
        return MockMcpSession(self.servers[server_name], self.datasets)
