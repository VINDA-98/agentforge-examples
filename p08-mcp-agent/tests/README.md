# 测试目录说明

本目录验证 `p08-mcp-agent` 的接入链路。

## 当前覆盖
- 可以连接已知 server
- 可以发现工具
- 可以根据问题完成一次工具调用
- server 不存在时会抛出明确错误

## 运行命令
```bash
python3 -m unittest discover tests
```
