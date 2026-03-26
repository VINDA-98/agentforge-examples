# p07-multi-agent-team

## 项目导航速览

- 项目目标：用多个角色分工完成同一任务，理解协调者、规划者、研究者和审阅者的协作边界。
- 对应章节：[第 9 章](../../docs/ch09-multi-agent/)
- 适合什么时候做：建议在完成第 9 章后动手，先建立“什么时候值得拆角色”的判断再做协作实现。
- 启动方式：进入目录后执行 `python3 src/main.py --brief "请为新手学员设计一次多智能体协作工作坊，本周五前交付活动方案"`。
- GitHub 查看源码 / 下载代码：公开示例仓库项目目录，[p07-multi-agent-team](https://github.com/VINDA-98/agentforge-examples/tree/main/p07-multi-agent-team)
- 说明：文档站部署来自私有主仓库；网站中的下载入口统一跳到公开示例仓库。
- 返回导航：[学习路径](../../docs/learning-path.md) · [章节索引](../../docs/chapter-index.md) · [项目总览](../../docs/project-overview.md)

## 项目目标
这个项目解决“什么时候应该把任务拆给多个 Agent 协作”这个问题。你会得到一个最小 Multi-Agent（多智能体协作）示例：协调者把任务交给规划、调研、写作、审阅四个角色，再把它们的结果整合成最终方案。

## 适合配套学习的章节
- 第 9 章：Multi-Agent（多智能体协作）

## 适合谁
- 已经理解 Workflow（工作流）与步骤编排
- 想进一步理解“角色分工”和“消息流转”的学员

## 项目范围
本项目会做：
- 定义 4 个不同职责的 Agent 角色
- 让各角色围绕同一个 brief 进行协作
- 记录消息流转过程
- 在信息缺失时由审阅角色要求返工
- 提供 `starter/` 和 `solution/` 对照版本

本项目不做：
- 真实大模型之间的多轮对话
- 并发执行框架
- 跨网络协作
- 权限系统

## 项目场景
项目使用“课程活动策划团队”场景。协调者收到 brief 后，会依次调用：
- `planner`：拆分目标和步骤
- `researcher`：补充经验和规则
- `writer`：生成方案草稿
- `reviewer`：检查方案是否能执行

## 安装步骤
```bash
cd projects/p07-multi-agent-team
cp .env.example .env
python3 -m pip install -r requirements.txt
```

## 运行命令
运行主线实现：
```bash
python3 src/main.py --brief "请为新手学员设计一次多智能体协作工作坊，本周五前交付活动方案"
python3 src/main.py --brief "请设计一次多智能体协作工作坊"
```

运行测试：
```bash
python3 -m unittest discover tests
```

查看练习起点：
```bash
python3 starter/main.py --brief "请为新手学员设计一次多智能体协作工作坊，本周五前交付活动方案"
```

查看参考实现：
```bash
python3 solution/main.py --brief "请为新手学员设计一次多智能体协作工作坊，本周五前交付活动方案"
```

## 预期输出
运行第一条主线命令后，你会看到类似输出：

```text
协作状态：ready
消息记录：
1. coordinator -> planner：请为新手学员设计一次多智能体协作工作坊，本周五前交付活动方案
2. planner -> coordinator：目标受众=新手学员；截止时间=本周五；任务数=4
3. researcher -> coordinator：建议强调收益、演示结果和复盘安排。
4. writer -> coordinator：已生成活动方案草稿。
5. reviewer -> coordinator：草稿通过，可以进入执行。

最终方案：
项目主题：多智能体协作工作坊
目标受众：新手学员
时间线：本周五
交付物：活动方案、宣传文案、复盘记录
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了“规划角色”“调研角色”“审阅角色”的 `TODO`
- `solution/main.py`：给出一个更短的角色协作版本
- `src/`：项目主线版本，包含更清晰的消息结构和协调类

## 目录说明
```text
projects/p07-multi-agent-team/
├── README.md
├── .env.example
├── requirements.txt
├── data/
│   ├── README.md
│   └── team_knowledge.json
├── src/
│   ├── README.md
│   ├── agents.py
│   ├── main.py
│   └── team_orchestrator.py
├── tests/
│   ├── README.md
│   └── test_smoke.py
├── starter/
│   ├── README.md
│   └── main.py
└── solution/
    ├── README.md
    └── main.py
```

## 验收标准
- 运行后能看到多个角色的协作记录
- 信息完整时可以输出可执行方案
- 信息缺失时会返回“需要补充信息”或“需要修改”
- `python3 -m unittest discover tests` 可以通过
- 学员能看懂为什么这里要用多智能体，而不是单个大函数

## 常见问题
### 1. 为什么这里要拆 4 个角色？
为了让学员看到“不同职责分工”带来的好处。规划、调研、写作、审阅关注点不同，拆开后更容易修改和扩展。

### 2. 这是不是一定比单 Agent 更好？
不是。任务很小时，多智能体反而更复杂。这个项目的重点是理解适用边界，而不是默认“角色越多越高级”。

### 3. 为什么消息流转还是顺序执行？
因为当前目标是教学清晰，不是并发优化。先把协作边界看懂，再谈并发和调度。
