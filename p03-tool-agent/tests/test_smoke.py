from __future__ import annotations

from pathlib import Path
import sys
import unittest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from tool_agent import ToolAgent


class ToolAgentSmokeTest(unittest.TestCase):
    def setUp(self) -> None:
        faq_path = Path(__file__).resolve().parents[1] / "data" / "course_faq.json"
        self.agent = ToolAgent(str(faq_path))

    def test_calculator_tool_is_selected(self) -> None:
        result = self.agent.run("请计算 12 + 30")
        self.assertEqual(result.selected_tool, "calculator")
        self.assertEqual(result.tool_output, 42.0)

    def test_course_lookup_tool_is_selected(self) -> None:
        result = self.agent.run("什么是 Tool Calling")
        self.assertEqual(result.selected_tool, "course_lookup")
        self.assertIn("工具", str(result.tool_output))


if __name__ == "__main__":
    unittest.main()
