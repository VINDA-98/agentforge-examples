from __future__ import annotations

import argparse
from pathlib import Path

from workflow_agent import WorkflowAgent


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
    parser = argparse.ArgumentParser(description="运行一个最小 Workflow agent。")
    parser.add_argument(
        "--request",
        default="请帮我规划一次面向新手学员的 Workflow 实战直播，本周五发布报名页",
        help="用户的任务请求",
    )
    parser.add_argument("--env-file", default=".env", help="配置文件路径")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    env_values = load_env_values(args.env_file)
    template_path = env_values.get("WORKFLOW_TEMPLATE_FILE", "data/workflow_templates.json")

    agent = WorkflowAgent(template_path=template_path)
    result = agent.run(args.request)

    print(f"工作流状态：{result.status}")
    print("步骤记录：")
    for index, step in enumerate(result.steps, start=1):
        print(f"{index}. {step.name} [{step.status}] {step.detail}")

    print()
    if result.plan:
        print("执行计划：")
        for item in result.plan:
            print(f"- {item}")
        print()

    print(f"总结：{result.summary}")
    print(f"下一步：{result.next_action}")


if __name__ == "__main__":
    main()
