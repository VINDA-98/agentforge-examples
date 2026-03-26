from __future__ import annotations

import argparse


SERVERS = {
    "course_ops": {
        "get_project_status": lambda arguments: {
            "project_key": arguments["project_key"],
            "status": "联调中",
        }
    }
}


def answer_question(question: str) -> str:
    if "p08" in question.lower():
        result = SERVERS["course_ops"]["get_project_status"]({"project_key": "p08"})
        return f"项目 {result['project_key']} 当前状态是{result['status']}。"
    return "没有找到合适的工具。"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="solution 版本的 MCP 风格接入项目。")
    parser.add_argument("--question", default="p08 项目现在是什么状态？")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(answer_question(args.question))


if __name__ == "__main__":
    main()
