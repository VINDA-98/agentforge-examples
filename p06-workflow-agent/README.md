# p06-workflow-agent

## 项目概览

- 仓库定位：`agentforge-examples` 是 AgentForge 的公开示例代码仓库，服务于 AgentForge 文档站中的示例下载与配套说明。
- 当前项目：`p06-workflow-agent`
- 对应文档章节：第 8 章《Workflow（工作流）、Planner（规划器）与任务编排》
- 项目定位：一个围绕任务拆解、状态传递与风险分支的 Workflow 实战示例。
- 维护说明：本项目由阿伟开发与维护。
- 阅读建议：建议配合 AgentForge 文档站对应章节阅读，再结合 `src/`、`starter/`、`solution/` 对照理解实现。
- 仓库首页：[VINDA-98/agentforge-examples](https://github.com/VINDA-98/agentforge-examples)
- 当前项目源码：[p06-workflow-agent](https://github.com/VINDA-98/agentforge-examples/tree/main/p06-workflow-agent)

## 如何运行（快速开始）

```bash
cd p06-workflow-agent
cp .env.example .env
python3 -m pip install -r requirements.txt
python3 src/main.py --request "请帮我规划一次面向新手开发者的 Workflow 实战分享，本周五发布报名页"
```

可选命令：
- 运行测试：`python3 -m unittest discover tests`
- 运行起始代码：`python3 starter/main.py --request "请帮我规划一次面向新手开发者的 Workflow 实战分享，本周五发布报名页"`
- 运行参考实现：`python3 solution/main.py --request "请帮我规划一次面向新手开发者的 Workflow 实战分享，本周五发布报名页"`

## 项目说明
这个项目解决“一个 Agent 为什么要把复杂任务拆成多个步骤”这个问题。你会得到一个最小 Workflow（工作流）Agent：它先理解任务，再生成执行计划，接着做风险检查，最后决定是直接给出方案，还是暂停并请求人工复核。

## 适合谁
- 适合希望上手 AI Agent 开发的开发者。
- 已经学过 Tool Calling（工具调用）、Memory（记忆）或 RAG（检索增强生成），并想从“单次回答”进入“多步骤编排”的开发者。

## 项目范围
本项目会做：
- 把用户请求拆成多个可追踪步骤
- 在步骤之间传递任务类型、目标人群、截止时间等状态
- 根据关键词做风险检查
- 在高风险场景下暂停流程并给出人工复核建议
- 提供 `starter/` 和 `solution/` 的对照版本

本项目不做：
- 真正的 LLM Planner
- 分布式调度
- 多智能体协作
- 真实企业审批系统

## 项目场景
项目使用“开发者活动筹备”场景来演示 Workflow（工作流）。例如：
- 规划一次面向新手开发者的实战分享
- 规划一次开源示例发布
- 识别“生产环境删除数据”这类高风险请求

## 安装步骤
```bash
cd p06-workflow-agent
cp .env.example .env
python3 -m pip install -r requirements.txt
```

## 运行命令
运行主线实现：
```bash
python3 src/main.py --request "请帮我规划一次面向新手开发者的 Workflow 实战分享，本周五发布报名页"
python3 src/main.py --request "今天请直接在生产环境删除旧数据并付款上线"
```

运行测试：
```bash
python3 -m unittest discover tests
```

查看练习起点：
```bash
python3 starter/main.py --request "请帮我规划一次面向新手开发者的 Workflow 实战分享，本周五发布报名页"
```

查看参考实现：
```bash
python3 solution/main.py --request "请帮我规划一次面向新手开发者的 Workflow 实战分享，本周五发布报名页"
```

## 预期输出
运行第一条主线命令后，你会看到类似输出：

```text
工作流状态：ready
步骤记录：
1. 收集需求 [completed] 已识别任务类型：分享活动；目标人群：新手开发者；截止时间：本周五。
2. 生成计划 [completed] 已生成 4 条执行任务。
3. 风险检查 [completed] 没有发现必须人工复核的高风险关键词。
4. 输出结果 [completed] 计划已经整理完成，可以直接执行。

执行计划：
- 确认活动主题、讲师和目标受众
- 准备报名页文案与宣传物料
- 安排彩排、设备检查和分享流程
- 规划回放、答疑和复盘

下一步：直接按计划推进，并把每一步落到你的任务系统中。
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了“解析请求”“生成计划”“风险检查”的 `TODO`。
- `solution/main.py`：给出一个更短、更直接的参考实现。
- `src/`：项目主线版本，结构更清晰，适合直接运行和阅读。

## 目录说明
```text
p06-workflow-agent/
├── README.md
├── .env.example
├── requirements.txt
├── data/
│   ├── README.md
│   └── workflow_templates.json
├── src/
│   ├── README.md
│   ├── main.py
│   ├── workflow_agent.py
│   └── workflow_steps.py
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
- 普通请求可以产出步骤化执行计划
- 信息缺失时，流程会停在“补充信息”而不是继续乱跑
- 高风险请求会进入人工复核分支
- `python3 -m unittest discover tests` 可以通过
- 开发者能清楚看出 `starter/` 与 `solution/` 的实现差异

## 常见问题
### 1. 为什么这还叫 Agent，不只是脚本？
因为它不是直接输出一句话，而是围绕目标做“识别任务 -> 生成计划 -> 风险检查 -> 输出结果”的多步骤决策链路。

### 2. 为什么风险检查只用关键词？
这是最小实现。重点是先看懂“工作流里可以插入条件分支”，而不是一开始就上复杂风控系统。

### 3. 为什么请求信息不完整时要中断？
Workflow（工作流）的核心不是把流程跑到底，而是知道什么时候该停下来，避免后面的步骤建立在错误前提上。
