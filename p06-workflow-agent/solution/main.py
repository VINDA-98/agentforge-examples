from __future__ import annotations

import argparse


PLAN_TEMPLATES = {
    "直播": ["确定直播主题", "准备报名页", "安排彩排", "整理回放和复盘"],
    "发布": ["确认上线范围", "检查发布清单", "安排通知节奏", "收集反馈"],
}
RISK_KEYWORDS = ["生产环境", "删除", "付款"]


def build_plan(request: str) -> list[str]:
    for keyword, tasks in PLAN_TEMPLATES.items():
        if keyword in request:
            return tasks
    return ["明确目标", "拆分步骤", "安排时间", "整理风险"]


def review_risk(request: str) -> list[str]:
    return [keyword for keyword in RISK_KEYWORDS if keyword in request]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="solution 版本的 Workflow agent。")
    parser.add_argument("--request", default="请帮我规划一次面向新手学员的 Workflow 实战直播，本周五发布报名页")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    plan = build_plan(args.request)
    risks = review_risk(args.request)

    print("执行计划：")
    for item in plan:
        print(f"- {item}")

    if risks:
        print(f"风险提醒：{', '.join(risks)}，请人工复核。")
    else:
        print("风险提醒：未发现必须人工复核的关键词。")


if __name__ == "__main__":
    main()
