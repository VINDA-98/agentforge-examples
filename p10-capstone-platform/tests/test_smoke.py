from __future__ import annotations

from pathlib import Path
import sys
import unittest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from platform_service import PlatformService


class PlatformServiceSmokeTest(unittest.TestCase):
    def setUp(self) -> None:
        data_file = Path(__file__).resolve().parents[1] / "data" / "platform_catalog.json"
        self.service = PlatformService(str(data_file))

    def test_health(self) -> None:
        health = self.service.health()
        self.assertEqual(health["status"], "ok")
        self.assertEqual(health["agent_count"], 3)

    def test_faq_request(self) -> None:
        result = self.service.handle_request("faq", "p10 项目适用于哪些章节？")
        self.assertEqual(result["agent"], "faq")
        self.assertIn("第 13-16 章", result["output"])

    def test_invalid_request_type_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            self.service.handle_request("unknown", "test")


if __name__ == "__main__":
    unittest.main()
