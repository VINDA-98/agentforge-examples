from __future__ import annotations

import argparse


def planner(brief: str) -> str:
    return f"规划结果：围绕“{brief}”准备主题、时间线、交付物。"


def researcher(brief: str) -> str:
    if "新手" in brief:
        return "调研结果：要强调收益、演示和复盘。"
    return "调研结果：至少写清目标和时间线。"


def reviewer(brief: str) -> str:
    if "周" not in brief and "今天" not in brief and "明天" not in brief:
        return "审阅结果：需要补充截止时间。"
    return "审阅结果：方案可执行。"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="solution 版本的多智能体协作项目。")
    parser.add_argument("--brief", default="请为新手学员设计一次多智能体协作工作坊，本周五前交付活动方案")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(planner(args.brief))
    print(researcher(args.brief))
    print(reviewer(args.brief))


if __name__ == "__main__":
    main()
