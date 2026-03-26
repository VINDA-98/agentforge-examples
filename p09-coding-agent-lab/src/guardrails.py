from __future__ import annotations

from pathlib import Path


BLOCKED_REQUEST_HINTS = {
    "rm -rf": "禁止执行破坏性删除命令。",
    "删除整个项目": "禁止删除整个项目。",
    "读取 .env": "禁止读取敏感配置文件。",
    "泄露密钥": "禁止请求泄露密钥。",
}
ALLOWED_SUFFIXES = {".py", ".md", ".json"}


def check_request_text(request: str) -> list[str]:
    reasons = []
    for keyword, reason in BLOCKED_REQUEST_HINTS.items():
        if keyword in request:
            reasons.append(reason)
    return reasons


def validate_target_file(file_path: str, allowed_root: str) -> list[str]:
    reasons: list[str] = []
    target_path = Path(file_path).resolve()
    root_path = Path(allowed_root).resolve()

    if root_path not in target_path.parents and target_path != root_path:
        reasons.append("目标文件超出了允许读取的目录范围。")

    if target_path.suffix not in ALLOWED_SUFFIXES:
        reasons.append("当前只允许读取 .py、.md、.json 文件。")

    if target_path.name.startswith(".env"):
        reasons.append("不允许读取 .env 类敏感配置文件。")

    if not target_path.exists():
        reasons.append("目标文件不存在。")

    return reasons
