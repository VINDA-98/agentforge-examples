# 数据目录说明

本目录放 `p08-mcp-agent` 的 mock server 配置。

## 当前文件
- `mcp_servers.json`：server 清单、工具描述和样例数据

## 使用方式
- `src/mock_mcp_server.py` 会把这个文件当作“外部系统描述”
- 你可以增加新工具，练习如何扩展接入层
