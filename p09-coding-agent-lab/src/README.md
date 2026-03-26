# 源码目录说明

`src/` 放项目主线实现。

## 文件说明
- `main.py`：命令行入口，支持 `analyze` 和 `eval`
- `guardrails.py`：拦截危险请求和越界文件
- `coding_agent.py`：读取文件并给出修复建议
- `eval_runner.py`：执行最小评测

## 建议阅读顺序
1. 先看 `guardrails.py`
2. 再看 `coding_agent.py`
3. 最后运行 `main.py analyze` 和 `main.py eval`
