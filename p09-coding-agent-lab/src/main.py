from __future__ import annotations

import argparse
from pathlib import Path

from coding_agent import CodingAgent
from eval_runner import EvalRunner


def load_env_values(env_file: str) -> dict[str, str]:
    values: dict[str, str] = {}
    env_path = Path(env_file)
    if not env_path.exists():
        return values

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="运行一个最小编码智能体实验项目。")
    parser.add_argument("--env-file", default=".env", help="配置文件路径")

    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze_parser = subparsers.add_parser("analyze", help="分析样例代码")
    analyze_parser.add_argument("--file", default="data/sample_buggy_module.py", help="目标文件路径")
    analyze_parser.add_argument("--request", default="请检查这个 Python 文件里的问题", help="用户请求")

    subparsers.add_parser("eval", help="运行最小评测")
    return parser


def run_analyze(agent: CodingAgent, file_path: str, request: str) -> None:
    report = agent.analyze(request, file_path)

    if report.blocked:
        print("护栏状态：已拦截")
        print("拦截原因：")
        for reason in report.block_reasons:
            print(f"- {reason}")
        return

    print("护栏状态：通过")
    print(f"分析总结：{report.summary}")
    print("发现的问题：")
    for index, item in enumerate(report.findings, start=1):
        print(f"{index}. {item}")

    print()
    print("修复建议：")
    for index, item in enumerate(report.suggestions, start=1):
        print(f"{index}. {item}")


def run_eval(agent: CodingAgent, cases_path: str, project_root: str) -> None:
    runner = EvalRunner(agent, cases_path, project_root)
    summary = runner.run()

    print(f"评测通过：{summary.passed}/{summary.total}")
    for result in summary.results:
        status = "PASS" if result.passed else "FAIL"
        print(f"- {status} {result.name}：{result.detail}")


def main() -> None:
    args = build_parser().parse_args()
    env_values = load_env_values(args.env_file)

    allowed_root = env_values.get("AGENT_ALLOWED_ROOT", "data")
    cases_path = env_values.get("EVAL_CASES_FILE", "data/eval_cases.json")
    project_root = Path(__file__).resolve().parents[1]
    agent = CodingAgent(str(project_root / allowed_root))

    if args.command == "analyze":
        run_analyze(agent, str(project_root / args.file), args.request)
        return

    run_eval(agent, str(project_root / cases_path), str(project_root))


if __name__ == "__main__":
    main()
