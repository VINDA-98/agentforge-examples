from __future__ import annotations

import argparse


def extract_context(request: str) -> dict[str, str]:
    # TODO 1: 从 request 中提取任务类型、目标人群和截止时间
    raise NotImplementedError("请先完成 extract_context()。")


def make_plan(context: dict[str, str]) -> list[str]:
    # TODO 2: 根据 context 生成执行计划
    raise NotImplementedError("请先完成 make_plan()。")


def review_risk(request: str) -> list[str]:
    # TODO 3: 返回命中的风险关键词说明
    raise NotImplementedError("请先完成 review_risk()。")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="starter 版本的 Workflow agent。")
    parser.add_argument("--request", default="请帮我规划一次面向新手学员的 Workflow 实战直播，本周五发布报名页")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        context = extract_context(args.request)
        plan = make_plan(context)
        risks = review_risk(args.request)
        print(f"上下文：{context}")
        print(f"计划：{plan}")
        print(f"风险：{risks}")
    except NotImplementedError as error:
        print("starter 版本还没有完成。")
        print(error)


if __name__ == "__main__":
    main()
