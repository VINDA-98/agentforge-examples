from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from guardrails import check_request_text, validate_target_file


@dataclass
class CodingReport:
    blocked: bool
    summary: str
    findings: list[str]
    suggestions: list[str]
    block_reasons: list[str]


class CodingAgent:
    def __init__(self, allowed_root: str):
        self.allowed_root = allowed_root

    def analyze(self, request: str, file_path: str) -> CodingReport:
        block_reasons = check_request_text(request)
        block_reasons.extend(validate_target_file(file_path, self.allowed_root))
        if block_reasons:
            return CodingReport(
                blocked=True,
                summary="请求已被护栏拦截。",
                findings=[],
                suggestions=[],
                block_reasons=block_reasons,
            )

        code = Path(file_path).read_text(encoding="utf-8")
        findings: list[str] = []
        suggestions: list[str] = []

        if "print(" in code:
            findings.append("检测到调试输出 print(...)，建议在提交前移除。")
            suggestions.append("删除或替换调试输出为正式日志。")

        if "/" in code:
            findings.append("检测到直接除法，建议补充零值检查。")
            suggestions.append("在除法前增加零值检查，例如先判断 if b == 0。")

        if "except Exception" in code and "pass" in code:
            findings.append("检测到 except Exception 后直接 pass，容易吞掉错误。")
            suggestions.append("不要直接 pass，至少返回明确错误或重新抛出异常。")

        if "TODO" in code:
            findings.append("检测到 TODO 注释，说明还有未完成逻辑。")
            suggestions.append("在提交前补齐 TODO 对应逻辑，或把范围写进 README。")

        if not findings:
            findings.append("没有发现明显问题。")
            suggestions.append("可以补充更多测试用例，验证主流程和边界场景。")

        return CodingReport(
            blocked=False,
            summary=f"发现 {len(findings)} 个需要优先处理的问题。",
            findings=findings,
            suggestions=suggestions,
            block_reasons=[],
        )
