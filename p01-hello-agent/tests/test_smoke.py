from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from config import AgentConfig
from hello_agent import HelloAgent


class HelloAgentSmokeTest(unittest.TestCase):
    def test_agent_response_contains_name_and_task(self) -> None:
        config = AgentConfig(agent_name="课程助理", agent_style="清晰", default_task="默认任务")
        agent = HelloAgent(config)

        result = agent.run("小李", "学习 Agent 基础")

        self.assertIn("小李", result.response)
        self.assertIn("学习 Agent 基础", result.response)
        self.assertIn("课程助理", result.response)

    def test_load_config_from_env_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            env_file = Path(temp_dir) / ".env"
            env_file.write_text(
                "AGENT_NAME=测试 Agent\nAGENT_STYLE=耐心\nDEFAULT_TASK=练习命令行\n",
                encoding="utf-8",
            )

            config = AgentConfig.load(str(env_file))

        self.assertEqual(config.agent_name, "测试 Agent")
        self.assertEqual(config.agent_style, "耐心")
        self.assertEqual(config.default_task, "练习命令行")


if __name__ == "__main__":
    unittest.main()
