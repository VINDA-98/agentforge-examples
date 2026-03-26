from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from memory_agent import MemoryAgent
from memory_store import ConversationMemory


class MemoryAgentSmokeTest(unittest.TestCase):
    def test_agent_can_remember_name_and_goal(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            memory_file = Path(temp_dir) / "memory.json"
            memory = ConversationMemory(str(memory_file), max_history=6)
            agent = MemoryAgent(memory)

            agent.handle_message("demo", "我叫小王")
            agent.handle_message("demo", "我想学 Tool Calling")
            result = agent.handle_message("demo", "你还记得我叫什么吗？")

        self.assertIn("小王", result.reply)
        self.assertEqual(result.profile["goal"], "Tool Calling")


if __name__ == "__main__":
    unittest.main()
