# 源码目录说明

`src/` 放项目主线实现，适合学员直接运行和阅读。

## 文件说明
- `main.py`：命令行入口，负责读取参数并打印结果
- `workflow_agent.py`：工作流主类，负责串起每个步骤
- `workflow_steps.py`：放任务识别、模板加载和风险检查等步骤函数

## 建议阅读顺序
1. 先看 `main.py`，理解程序怎么启动
2. 再看 `workflow_agent.py`，理解工作流主链路
3. 最后看 `workflow_steps.py`，理解每一步怎么做
