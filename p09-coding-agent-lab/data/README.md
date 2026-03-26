# 数据目录说明

本目录放 `p09-coding-agent-lab` 的样例代码和评测用例。

## 当前文件
- `sample_buggy_module.py`：带有典型问题的样例代码
- `eval_cases.json`：评测输入与期望输出

## 使用方式
- `coding_agent.py` 读取样例代码进行分析
- `eval_runner.py` 会按 `eval_cases.json` 执行最小评测
