from __future__ import annotations

from pathlib import Path
import sys
import unittest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from rag_agent import RagAgent


class RagAgentSmokeTest(unittest.TestCase):
    def setUp(self) -> None:
        knowledge_path = Path(__file__).resolve().parents[1] / "data" / "knowledge_base.json"
        self.agent = RagAgent(str(knowledge_path), top_k=2)

    def test_related_question_returns_passages(self) -> None:
        result = self.agent.answer("RAG 为什么要先检索？")
        self.assertTrue(result.passages)
        self.assertIn("检索", result.answer)

    def test_unrelated_question_returns_fallback(self) -> None:
        result = self.agent.answer("怎么煮一杯咖啡？")
        self.assertEqual(result.passages, [])
        self.assertIn("没有找到", result.answer)


if __name__ == "__main__":
    unittest.main()
