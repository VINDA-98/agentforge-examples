from __future__ import annotations

from pathlib import Path
import sys
import unittest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from team_orchestrator import MultiAgentTeam


class MultiAgentTeamSmokeTest(unittest.TestCase):
    def setUp(self) -> None:
        knowledge_path = Path(__file__).resolve().parents[1] / "data" / "team_knowledge.json"
        self.team = MultiAgentTeam(str(knowledge_path))

    def test_complete_brief_returns_ready(self) -> None:
        result = self.team.collaborate("请为新手学员设计一次多智能体协作工作坊，本周五前交付活动方案")
        self.assertEqual(result.status, "ready")
        self.assertIn("时间线：本周五", result.final_output)
        self.assertFalse(result.review_notes)

    def test_missing_brief_info_returns_revision(self) -> None:
        result = self.team.collaborate("请设计一次多智能体协作工作坊")
        self.assertEqual(result.status, "needs_revision")
        self.assertTrue(result.review_notes)
        self.assertIn("缺少明确截止时间", result.review_notes[0])


if __name__ == "__main__":
    unittest.main()
