# 源码目录说明

`src/` 放项目主线实现。

## 文件说明
- `main.py`：命令行入口
- `agents.py`：定义规划、调研、写作、审阅四个角色
- `team_orchestrator.py`：定义协调者，负责串起消息流转

## 建议阅读顺序
1. 先看 `team_orchestrator.py`
2. 再看 `agents.py`
3. 最后运行 `main.py` 观察消息输出
