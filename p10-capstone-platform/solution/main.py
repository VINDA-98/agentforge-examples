from __future__ import annotations

import argparse


def faq_agent(message: str) -> str:
    if "章节" in message:
        return "p10 主要对应第 13-16 章。"
    return "请补充更具体的问题。"


def plan_agent(message: str) -> str:
    return f"建议先明确目标，再围绕“{message}”做最小演示。"


def review_agent(message: str) -> str:
    return f"请检查目标用户、运行命令、测试入口和验收标准。当前请求：{message}"


def route_request(request_type: str, message: str) -> str:
    routes = {
        "faq": faq_agent,
        "plan": plan_agent,
        "review": review_agent,
    }
    return routes.get(request_type, lambda _: "不支持的请求类型。")(message)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="solution 版本的毕业项目平台。")
    parser.add_argument("--request-type", default="faq")
    parser.add_argument("--message", default="p10 项目适用于哪些章节？")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(route_request(args.request_type, args.message))


if __name__ == "__main__":
    main()
