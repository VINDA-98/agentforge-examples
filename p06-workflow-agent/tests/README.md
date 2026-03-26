# 测试目录说明

本目录验证 `p06-workflow-agent` 的关键路径。

## 当前覆盖
- 普通请求可以生成计划
- 信息缺失时会进入补充信息分支
- 高风险请求会进入人工复核分支

## 运行命令
```bash
python3 -m unittest discover tests
```
