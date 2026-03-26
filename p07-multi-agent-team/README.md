# p07-multi-agent-team

## 项目概览

- 仓库定位：`agentforge-examples` 是 AgentForge 的公开示例代码仓库，服务于 AgentForge 文档站中的示例下载与配套说明。
- 当前项目：`p07-multi-agent-team`
- 对应文档章节：第 9 章《Multi-Agent（多智能体协作）》
- 项目定位：一个围绕角色分工与消息流转的 Multi-Agent 实战示例。
- 维护说明：本项目由阿伟开发与维护。
- 阅读建议：建议配合 AgentForge 文档站对应章节阅读，再结合 `src/`、`starter/`、`solution/` 对照理解实现。
- 仓库首页：[VINDA-98/agentforge-examples](https://github.com/VINDA-98/agentforge-examples)
- 当前项目源码：[p07-multi-agent-team](https://github.com/VINDA-98/agentforge-examples/tree/main/p07-multi-agent-team)

## 如何运行（快速开始）

```bash
cd p07-multi-agent-team
cp .env.example .env
python3 -m pip install -r requirements.txt
python3 src/main.py --brief "请为新手开发者设计一次多智能体协作工作坊，本周五前交付活动方案"
```

可选命令：
- 运行测试：`python3 -m unittest discover tests`
- 运行起始代码：`python3 starter/main.py --brief "请为新手开发者设计一次多智能体协作工作坊，本周五前交付活动方案"`
- 运行参考实现：`python3 solution/main.py --brief "请为新手开发者设计一次多智能体协作工作坊，本周五前交付活动方案"`

## 项目说明
这个项目解决“什么时候应该把任务拆给多个 Agent 协作”这个问题。你会得到一个最小 Multi-Agent（多智能体协作）示例：协调者把任务交给规划、调研、写作、审阅四个角色，再把它们的结果整合成最终方案。

## 适合谁
- 适合希望上手 AI Agent 开发的开发者。
- 已经理解 Workflow（工作流）与步骤编排，并想进一步理解“角色分工”和“消息流转”的开发者。

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
项目使用“示例协作团队”场景。协调者收到 brief 后，会依次调用：
- `planner`：拆分目标和步骤
- `researcher`：补充经验和规则
- `writer`：生成方案草稿
- `reviewer`：检查方案是否能执行

## 安装步骤
```bash
cd p07-multi-agent-team
cp .env.example .env
python3 -m pip install -r requirements.txt
```

## 运行命令
运行主线实现：
```bash
python3 src/main.py --brief "请为新手开发者设计一次多智能体协作工作坊，本周五前交付活动方案"
python3 src/main.py --brief "请设计一次多智能体协作工作坊"
```

运行测试：
```bash
python3 -m unittest discover tests
```

查看练习起点：
```bash
python3 starter/main.py --brief "请为新手开发者设计一次多智能体协作工作坊，本周五前交付活动方案"
```

查看参考实现：
```bash
python3 solution/main.py --brief "请为新手开发者设计一次多智能体协作工作坊，本周五前交付活动方案"
```

## 预期输出
运行第一条主线命令后，你会看到类似输出：

```text
协作状态：ready
消息记录：
1. coordinator -> planner：请为新手开发者设计一次多智能体协作工作坊，本周五前交付活动方案
2. planner -> coordinator：目标受众=新手开发者；截止时间=本周五；任务数=4
3. researcher -> coordinator：建议强调收益、演示结果和复盘安排。
4. writer -> coordinator：已生成活动方案草稿。
5. reviewer -> coordinator：草稿通过，可以进入执行。

最终方案：
项目主题：多智能体协作工作坊
目标受众：新手开发者
时间线：本周五
交付物：活动方案、宣传文案、复盘记录
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了“规划角色”“调研角色”“审阅角色”的 `TODO`。
- `solution/main.py`：给出一个更短的角色协作版本。
- `src/`：项目主线版本，包含更清晰的消息结构和协调类。

## 目录说明
```text
p07-multi-agent-team/
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

## 使用与署名
- 本项目由阿伟开发与维护。
- 适合希望上手 AI Agent 开发的开发者，并建议配合 AgentForge 文档站阅读。
- 允许个人学习与实践；引用或转载项目说明时，请保留作者署名“阿伟”和仓库地址：`https://github.com/VINDA-98/agentforge-examples`。

## 验收标准
- 运行后能看到多个角色的协作记录
- 信息完整时可以输出可执行方案
- 信息缺失时会返回“需要补充信息”或“需要修改”
- `python3 -m unittest discover tests` 可以通过
- 开发者能看懂为什么这里要用多智能体，而不是单个大函数

## 常见问题
### 1. 为什么这里要拆 4 个角色？
为了让开发者看到“不同职责分工”带来的好处。规划、调研、写作、审阅关注点不同，拆开后更容易修改和扩展。

### 2. 这是不是一定比单 Agent 更好？
不是。任务很小时，多智能体反而更复杂。这个项目的重点是理解适用边界，而不是默认“角色越多越高级”。

### 3. 为什么消息流转还是顺序执行？
因为当前目标是帮助你先看懂协作边界，而不是并发优化。先把协作边界看懂，再谈并发和调度。
