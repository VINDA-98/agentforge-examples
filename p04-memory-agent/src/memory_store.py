from __future__ import annotations

from pathlib import Path
import json


class ConversationMemory:
    def __init__(self, memory_file: str, max_history: int = 6):
        self.memory_file = Path(memory_file)
        self.max_history = max_history

    def load_all(self) -> dict[str, object]:
        if not self.memory_file.exists():
            return {}
        return json.loads(self.memory_file.read_text(encoding="utf-8"))

    def save_all(self, payload: dict[str, object]) -> None:
        self.memory_file.parent.mkdir(parents=True, exist_ok=True)
        self.memory_file.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def get_session(self, session_id: str) -> dict[str, object]:
        payload = self.load_all()
        session = payload.setdefault(session_id, {"profile": {}, "history": []})
        self.save_all(payload)
        return session

    def write_session(self, session_id: str, session_data: dict[str, object]) -> None:
        payload = self.load_all()
        payload[session_id] = session_data
        self.save_all(payload)

    def reset_session(self, session_id: str) -> None:
        payload = self.load_all()
        payload.pop(session_id, None)
        self.save_all(payload)
