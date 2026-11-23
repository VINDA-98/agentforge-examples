# AgentForge Examples

[English](README.md) · 简体中文

AgentForge 文档的配套代码库，收录 10 个 Python 实验。从最小命令行 Agent 开始，依次练习 JSON 校验、工具调用、记忆、检索和工作流编排，最后把这些能力放进一个小型服务。

每个实验都有独立的 README 和样例数据。先运行 `src/` 里的主线实现，再完成 `starter/` 里的练习，最后对照 `solution/`，用 `tests/` 里的冒烟测试验证行为。文档站对应章节提供背景和设计过程。

## 跑通第一个实验

第一个实验只用 Python 标准库，需要 Python 3.10 或更新版本。

```bash
git clone https://github.com/VINDA-98/agentforge-examples.git
cd agentforge-examples/p01-hello-agent
cp .env.example .env
python3 src/main.py --name 阿伟 --task "学习 Agent 基础"
python3 -m unittest discover tests
```

程序读取输入，生成格式固定的回复。跑通后可以先自己完成起始代码，再看参考实现。

## 实验目录

| 实验 | 文档章节 | 练习内容 |
| --- | --- | --- |
| [01 · Hello Agent](p01-hello-agent/) | 第 1、2、4 章 | 命令行输入、配置读取和稳定输出 |
| [02 · 结构化输出](p02-structured-output-lab/) | 第 3 章 | 生成任务卡片并校验 JSON 字段 |
| [03 · 工具调用](p03-tool-agent/) | 第 5 章 | 选择工具、执行调用和整理结果 |
| [04 · 会话记忆](p04-memory-agent/) | 第 6 章 | 存储和恢复会话上下文 |
| [05 · RAG](p05-rag-agent/) | 第 7 章 | 检索本地知识库，处理证据不足的情况 |
| [06 · 工作流](p06-workflow-agent/) | 第 8 章 | 任务拆解、状态传递和条件分支 |
| [07 · 多 Agent 协作](p07-multi-agent-team/) | 第 9 章 | 给不同角色分派任务并汇总输出 |
| [08 · MCP 接入](p08-mcp-agent/) | 第 10 章 | 用模拟 MCP 客户端练习工具发现和调用 |
| [09 · 编码 Agent](p09-coding-agent-lab/) | 第 11、12 章 | 模拟编码流程、护栏和评测 |
| [10 · 综合实战](p10-capstone-platform/) | 第 13–16 章 | 把前面的能力组合进最小服务 |

各实验的输入参数、预期行为和测试命令见对应 README。

## 作者与使用

示例由阿伟开发和维护，允许个人学习与实践。引用、转载或基于本仓库内容整理资料时，请保留作者署名“阿伟”和[原仓库地址](https://github.com/VINDA-98/agentforge-examples)。
