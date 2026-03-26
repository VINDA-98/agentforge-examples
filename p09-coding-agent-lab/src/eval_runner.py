from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

from coding_agent import CodingAgent


@dataclass
class EvalCaseResult:
    name: str
    passed: bool
    detail: str


@dataclass
class EvalSummary:
    passed: int
    total: int
    results: list[EvalCaseResult]


class EvalRunner:
    def __init__(self, agent: CodingAgent, cases_path: str, project_root: str):
        self.agent = agent
        self.cases_path = Path(cases_path)
        self.project_root = Path(project_root)

    def load_cases(self) -> list[dict[str, object]]:
        return json.loads(self.cases_path.read_text(encoding="utf-8"))

    def run(self) -> EvalSummary:
        results: list[EvalCaseResult] = []

        for case in self.load_cases():
            file_path = self.project_root / str(case["file"])
            report = self.agent.analyze(str(case["request"]), str(file_path))

            if case.get("expected_blocked"):
                passed = report.blocked
                detail = "已正确拦截危险请求。" if passed else "危险请求没有被拦截。"
            else:
                merged_text = " ".join(report.findings + report.suggestions + [report.summary])
                keywords = [str(item) for item in case["expected_keywords"]]
                passed = all(keyword in merged_text for keyword in keywords)
                detail = "输出包含全部期望关键词。" if passed else "输出缺少期望关键词。"

            results.append(
                EvalCaseResult(
                    name=str(case["name"]),
                    passed=passed,
                    detail=detail,
                )
            )

        passed_count = sum(1 for item in results if item.passed)
        return EvalSummary(passed=passed_count, total=len(results), results=results)
