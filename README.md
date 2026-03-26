# AgentForge Examples

`agentforge-examples` 是 AgentForge 的公开示例代码仓库，用于承接 AgentForge 文档站中的示例下载入口。仓库提供可直接浏览、克隆和运行的项目示例，适合作为外部开发者查阅与实践的公开代码集合。这里不包含完整文档站内容、私有主工程配置或站点部署细节。

## 仓库定位
- 公开范围：提供 `p01` 到 `p10` 的项目示例代码、项目级 README，以及 `starter/` 与 `solution/` 对照目录。
- 服务关系：本仓库服务于 AgentForge 文档站，作为各章节示例的公开代码仓库。
- 使用建议：建议先阅读 AgentForge 文档站对应章节，再进入本仓库查看项目 README、运行 `src/` 主线版本，并结合 `starter/` 与 `solution/` 对照理解实现。
- 不包含内容：完整文档站源码、私有工程配置、站点部署细节、内部制作文件。

## 作者与使用说明
- 本仓库中的示例项目由阿伟开发与维护。
- 仓库内容允许个人学习与实践使用。
- 引用、转载或基于本仓库内容整理资料时，请保留作者署名“阿伟”和仓库地址：`https://github.com/VINDA-98/agentforge-examples`。

## 建议学习顺序

| 顺序 | 项目 | 对应文档章节 | 核心主题 |
| --- | --- | --- | --- |
| 1 | [p01-hello-agent](./p01-hello-agent/) | 第 1、2、4 章 | 第一个最小可运行 Agent |
| 2 | [p02-structured-output-lab](./p02-structured-output-lab/) | 第 3 章 | 结构化输出与 JSON 校验 |
| 3 | [p03-tool-agent](./p03-tool-agent/) | 第 5 章 | Tool Calling（工具调用） |
| 4 | [p04-memory-agent](./p04-memory-agent/) | 第 6 章 | Memory（记忆与上下文恢复） |
| 5 | [p05-rag-agent](./p05-rag-agent/) | 第 7 章 | RAG（检索增强生成） |
| 6 | [p06-workflow-agent](./p06-workflow-agent/) | 第 8 章 | Workflow（工作流）与任务编排 |
| 7 | [p07-multi-agent-team](./p07-multi-agent-team/) | 第 9 章 | Multi-Agent（多智能体协作） |
| 8 | [p08-mcp-agent](./p08-mcp-agent/) | 第 10 章 | MCP（模型上下文协议）接入 |
| 9 | [p09-coding-agent-lab](./p09-coding-agent-lab/) | 第 11、12 章 | 编码智能体、护栏与评测 |
| 10 | [p10-capstone-platform](./p10-capstone-platform/) | 第 13 到第 16 章 | 综合平台骨架 |

## 如何使用这个仓库
1. 先在 AgentForge 文档站找到当前章节或项目，了解该示例要解决的问题和目标。
2. 再进入本仓库对应目录，查看项目 README、运行 `src/` 主线版本。
3. 完成主线运行后，再对照 `starter/` 和 `solution/` 做练习与复盘。
4. 如果你是从 AgentForge 文档站进入这里，直接打开对应项目目录即可开始。

## 如何运行单个项目
下面是所有项目通用的最小流程。具体命令参数以各项目 README 为准。

```bash
git clone https://github.com/VINDA-98/agentforge-examples.git
cd agentforge-examples
cd p01-hello-agent
cp .env.example .env
python -m pip install -r requirements.txt
python src/main.py --help
```

说明：
- 大多数项目使用 Python 3.10+ 即可运行。
- 如果你的环境里命令是 `python3`，请把上面的 `python` 替换成 `python3`。
- 每个项目 README 都单独写了“对应文档章节”“如何运行”“测试命令”和 `starter/solution` 对照说明。

## 项目列表
- `p01-hello-agent`：最小 Agent 输入、处理、输出闭环
- `p02-structured-output-lab`：结构化输出与字段校验
- `p03-tool-agent`：工具选择、执行与结果整理
- `p04-memory-agent`：会话记忆与上下文恢复
- `p05-rag-agent`：本地知识库检索与保守回答
- `p06-workflow-agent`：任务拆解、状态传递与风险分支
- `p07-multi-agent-team`：多角色协作与消息流转
- `p08-mcp-agent`：统一接入层、发现与调用外部能力
- `p09-coding-agent-lab`：编码智能体的工具、护栏与评测
- `p10-capstone-platform`：综合实战平台与最小服务骨架
