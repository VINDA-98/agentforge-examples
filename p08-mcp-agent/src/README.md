# 源码目录说明

`src/` 放项目主线实现。

## 文件说明
- `main.py`：命令行入口
- `mock_mcp_server.py`：本地 mock server、session 和 client
- `mcp_agent.py`：根据问题选择 server 和工具，并整理最终回答

## 建议阅读顺序
1. 先看 `mock_mcp_server.py`
2. 再看 `mcp_agent.py`
3. 最后运行 `main.py`
