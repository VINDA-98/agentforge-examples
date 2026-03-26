from __future__ import annotations

import argparse
import json
from pathlib import Path

from config import load_config
from platform_service import PlatformService
from server import run_server


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="运行毕业项目平台最小骨架。")
    parser.add_argument("--env-file", default=".env", help="配置文件路径")
    parser.add_argument("--mode", choices=["demo", "serve"], default="demo", help="运行模式")
    parser.add_argument("--request-type", default="faq", help="请求类型：faq / plan / review")
    parser.add_argument("--message", default="p10 项目适用于哪些章节？", help="用户请求")
    parser.add_argument("--host", help="覆盖监听地址")
    parser.add_argument("--port", type=int, help="覆盖监听端口")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    config = load_config(args.env_file)
    project_root = Path(__file__).resolve().parents[1]
    service = PlatformService(str(project_root / config.data_file))

    host = args.host or config.host
    port = args.port or config.port

    if args.mode == "serve":
        run_server(host, port, service)
        return

    result = service.handle_request(args.request_type, args.message)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
