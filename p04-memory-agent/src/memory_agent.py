from __future__ import annotations

from dataclasses import dataclass
import re

from memory_store import ConversationMemory


@dataclass
class AgentReply:
    reply: str
    profile: dict[str, str]
    history_count: int


class MemoryAgent:
    def __init__(self, memory: ConversationMemory):
        self.memory = memory

    def extract_profile_updates(self, message: str) -> dict[str, str]:
        updates: dict[str, str] = {}

        name_match = re.search(r"(?:我叫|我的名字是)(?!什么)([\u4e00-\u9fa5A-Za-z0-9_-]+)", message)
        if name_match:
            updates["name"] = name_match.group(1)

        goal_match = re.search(r"(?:我想学|我正在学|我最近在学)(.+)", message)
        if goal_match:
            updates["goal"] = goal_match.group(1).strip("。！!？? ")

        return updates

    def build_reply(self, message: str, profile: dict[str, str]) -> str:
        name = profile.get("name")
        goal = profile.get("goal")

        if "记得我叫什么" in message or "我叫什么" in message:
            return f"记得，你叫{name}。" if name else "我还不知道你的名字，可以先告诉我。"

        if "我在学什么" in message or "记得我的学习目标" in message:
            return f"你现在想学 {goal}。" if goal else "我还没有记住你的学习目标。"

        if "我叫" in message or "我的名字是" in message:
            return f"记住了，你叫{name}。"

        if "我想学" in message or "我正在学" in message or "我最近在学" in message:
            return f"记住了，你现在想学 {goal}。"

        if name and goal:
            return f"{name}，我记得你正在学 {goal}。你刚刚说的是：{message}"
        if name:
            return f"{name}，我记住了你的名字。你刚刚说的是：{message}"
        return f"我已经记录了这条消息：{message}"

    def handle_message(self, session_id: str, message: str) -> AgentReply:
        session = self.memory.get_session(session_id)
        profile = dict(session.get("profile", {}))
        profile.update(self.extract_profile_updates(message))

        reply = self.build_reply(message, profile)
        history = list(session.get("history", []))
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": reply})
        history = history[-self.memory.max_history :]

        session["profile"] = profile
        session["history"] = history
        self.memory.write_session(session_id, session)

        return AgentReply(reply=reply, profile=profile, history_count=len(history))
