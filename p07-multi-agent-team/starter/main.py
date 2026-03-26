from __future__ import annotations

import argparse


def planner_agent(brief: str) -> str:
    # TODO 1: 返回任务拆解结果
    raise NotImplementedError("请先完成 planner_agent()。")


def researcher_agent(brief: str) -> str:
    # TODO 2: 返回调研补充内容
    raise NotImplementedError("请先完成 researcher_agent()。")


def reviewer_agent(draft: str) -> str:
    # TODO 3: 返回审阅结果
    raise NotImplementedError("请先完成 reviewer_agent()。")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="starter 版本的多智能体协作项目。")
    parser.add_argument("--brief", default="请为新手学员设计一次多智能体协作工作坊，本周五前交付活动方案")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        plan = planner_agent(args.brief)
        notes = researcher_agent(args.brief)
        review = reviewer_agent(plan + notes)
        print(plan)
        print(notes)
        print(review)
    except NotImplementedError as error:
        print("starter 版本还没有完成。")
        print(error)


if __name__ == "__main__":
    main()
