from __future__ import annotations

import argparse
from pathlib import Path

from mcp_agent import McpAgent
from mock_mcp_server import MockMcpClient


def load_env_values(env_file: str) -> dict[str, str]:
    values: dict[str, str] = {}
    env_path = Path(env_file)
    if not env_path.exists():
        return values

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="运行一个最小 MCP 风格接入层示例。")
    parser.add_argument("--question", default="p08 项目现在是什么状态？", help="用户问题")
    parser.add_argument("--env-file", default=".env", help="配置文件路径")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    env_values = load_env_values(args.env_file)
    data_path = env_values.get("MCP_DATA_FILE", "data/mcp_servers.json")

    agent = McpAgent(data_path)
    result = agent.answer_question(args.question)

    client = MockMcpClient(data_path)
    session = client.connect(result.server_name)

    print(f"连接的 server：{result.server_name}")
    print("发现的工具：")
    for tool in session.list_tools():
        print(f"- {tool.name}：{tool.description}")

    print()
    print(f"选择工具：{result.selected_tool}")
    print(f"工具参数：{result.arguments}")
    print(f"工具结果：{result.tool_result}")
    print()
    print(f"最终回答：{result.answer}")


if __name__ == "__main__":
    main()
