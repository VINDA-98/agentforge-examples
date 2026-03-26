from __future__ import annotations

from pathlib import Path
import json
import sys
import unittest

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from structured_output import build_task_card, load_note_text, validate_task_card


class StructuredOutputSmokeTest(unittest.TestCase):
    def test_sample_note_generates_valid_card(self) -> None:
        sample_path = Path(__file__).resolve().parents[1] / "data" / "sample_note.txt"
        note_text = load_note_text(str(sample_path))

        payload = build_task_card(note_text, owner="课程助教")
        is_valid, errors = validate_task_card(payload)

        self.assertTrue(is_valid)
        self.assertEqual(errors, [])
        self.assertEqual(payload["title"], "修复登录页报错")

    def test_invalid_card_is_rejected(self) -> None:
        invalid_path = Path(__file__).resolve().parents[1] / "data" / "invalid_card.json"
        payload = json.loads(invalid_path.read_text(encoding="utf-8"))

        is_valid, errors = validate_task_card(payload)

        self.assertFalse(is_valid)
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
