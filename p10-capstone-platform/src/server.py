from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json

from platform_service import PlatformService


def create_handler(service: PlatformService) -> type[BaseHTTPRequestHandler]:
    class PlatformHandler(BaseHTTPRequestHandler):
        def _send_json(self, payload: object, status_code: int = 200) -> None:
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status_code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format: str, *args: object) -> None:
            return

        def do_GET(self) -> None:
            if self.path == "/health":
                self._send_json(service.health())
                return
            if self.path == "/agents":
                self._send_json(service.list_agents())
                return
            self._send_json({"error": "not found"}, status_code=404)

        def do_POST(self) -> None:
            if self.path != "/tasks":
                self._send_json({"error": "not found"}, status_code=404)
                return

            raw_length = self.headers.get("Content-Length", "0")
            payload_length = int(raw_length)
            raw_body = self.rfile.read(payload_length).decode("utf-8") if payload_length else "{}"

            try:
                payload = json.loads(raw_body)
            except json.JSONDecodeError:
                self._send_json({"error": "invalid json"}, status_code=400)
                return

            try:
                result = service.handle_request(
                    str(payload.get("request_type", "")),
                    str(payload.get("message", "")),
                )
            except ValueError as error:
                self._send_json({"error": str(error)}, status_code=400)
                return

            self._send_json(result)

    return PlatformHandler


def run_server(host: str, port: int, service: PlatformService) -> None:
    server = ThreadingHTTPServer((host, port), create_handler(service))
    print(f"平台服务已启动：http://{host}:{port}")
    print("可用接口：GET /health, GET /agents, POST /tasks")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n收到停止信号，准备退出。")
    finally:
        server.server_close()
