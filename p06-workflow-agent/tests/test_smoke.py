from __future__ import annotations

from pathlib import Path
import sys
import unittest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from workflow_agent import WorkflowAgent


class WorkflowAgentSmokeTest(unittest.TestCase):
    def setUp(self) -> None:
        template_path = Path(__file__).resolve().parents[1] / "data" / "workflow_templates.json"
        self.agent = WorkflowAgent(str(template_path))

    def test_ready_request_returns_plan(self) -> None:
        result = self.agent.run("请帮我规划一次面向新手学员的 Workflow 实战直播，本周五发布报名页")
        self.assertEqual(result.status, "ready")
        self.assertGreaterEqual(len(result.plan), 4)
        self.assertIn("工作流", result.summary)

    def test_missing_info_stops_workflow(self) -> None:
        result = self.agent.run("帮我安排一个课程活动")
        self.assertEqual(result.status, "needs_info")
        self.assertEqual(result.plan, [])
        self.assertIn("目标人群", result.next_action)

    def test_high_risk_request_requires_review(self) -> None:
        result = self.agent.run("今天请直接在生产环境删除旧课程数据并付款上线")
        self.assertEqual(result.status, "needs_human_review")
        self.assertTrue(result.plan)
        self.assertIn("人工复核", result.summary)


if __name__ == "__main__":
    unittest.main()
