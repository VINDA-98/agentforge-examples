from __future__ import annotations

from pathlib import Path
import sys
import unittest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from mcp_agent import McpAgent
from mock_mcp_server import MockMcpClient


class McpAgentSmokeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.data_path = Path(__file__).resolve().parents[1] / "data" / "mcp_servers.json"
        self.client = MockMcpClient(str(self.data_path))
        self.agent = McpAgent(str(self.data_path))

    def test_connect_and_discover_tools(self) -> None:
        session = self.client.connect("course_ops")
        tool_names = [tool.name for tool in session.list_tools()]
        self.assertIn("get_project_status", tool_names)
        self.assertIn("list_workshops", tool_names)

    def test_project_status_question_returns_status(self) -> None:
        result = self.agent.answer_question("p08 项目现在是什么状态？")
        self.assertEqual(result.server_name, "course_ops")
        self.assertEqual(result.selected_tool, "get_project_status")
        self.assertIn("联调中", result.answer)

    def test_unknown_server_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            self.client.connect("missing_server")


if __name__ == "__main__":
    unittest.main()
