# p08-mcp-agent

## 项目导航速览

- 项目目标：通过统一接入层连接外部能力，跑通 MCP 风格的连接、发现、调用链路。
- 对应章节：[第 10 章](../../docs/ch10-mcp-integration/)
- 适合什么时候做：建议在完成第 10 章后动手，用项目理解本地工具调用和外部系统接入的边界差异。
- 启动方式：进入目录后执行 `python3 src/main.py --question "p08 项目现在是什么状态？"`。
- GitHub 查看源码 / 下载代码：公开示例仓库项目目录，[p08-mcp-agent](https://github.com/VINDA-98/agentforge-examples/tree/main/p08-mcp-agent)
- 说明：文档站部署来自私有主仓库；网站中的下载入口统一跳到公开示例仓库。
- 返回导航：[学习路径](../../docs/learning-path.md) · [章节索引](../../docs/chapter-index.md) · [项目总览](../../docs/project-overview.md)

## 项目目标
这个项目解决“Agent 怎么通过统一接入层访问外部系统”这个问题。你会得到一个最小 MCP 风格示例：程序先连接一个本地模拟服务端（mock server），再发现可用工具，最后执行工具调用并整理结果。

## 适合配套学习的章节
- 第 10 章：MCP（模型上下文协议）与外部系统接入

## 适合谁
- 已经理解 Tool Calling（工具调用）与 Workflow（工作流）
- 想知道“连接外部系统”和“本地函数调用”有什么边界差异的学员

## 项目范围
本项目会做：
- 提供一个最小 MCP 风格客户端
- 用本地 JSON 模拟服务端（server）与工具清单
- 支持连接、发现能力、调用工具三个动作
- 演示查询项目状态、列出工作坊、查询课程规范
- 提供 `starter/` 和 `solution/` 对照版本

本项目不做：
- 真实网络协议通信
- 真正的 MCP SDK
- OAuth 或企业权限系统
- 多个服务端（server）并发管理

## 先解释两个容易混淆的词
- `服务端（server）`：你可以把它理解成“对外提供工具和数据的一侧”。本项目里它是本地模拟出来的，不是真正联网服务。
- `mock server（模拟服务端）`：专门为了教学和测试准备的假服务。它的作用是让你先看懂连接、发现、调用链路，而不是一上来就被真实网络协议绊住。

## 项目场景
项目使用“课程工具接入层”场景：
- `course_ops`：查询项目状态和工作坊安排
- `course_policy`：查询课程规范

这能帮助学员理解：MCP（模型上下文协议）的关键不是“神秘新 API”，而是“用统一方式接入外部能力”。

## 安装步骤
```bash
cd projects/p08-mcp-agent
cp .env.example .env
python3 -m pip install -r requirements.txt
```

## 运行命令
运行主线实现：
```bash
python3 src/main.py --question "p08 项目现在是什么状态？"
python3 src/main.py --question "本周有哪些工作坊？"
python3 src/main.py --question "starter 目录应该怎么用？"
```

第一次运行建议按这个顺序来：

1. 先问项目状态，最容易看懂“连接 -> 发现 -> 调用”的完整链路。
2. 再问工作坊安排，验证同一个服务端能暴露多个工具。
3. 最后问课程规范，理解为什么不同服务端会提供不同能力。

运行测试：
```bash
python3 -m unittest discover tests
```

查看练习起点：
```bash
python3 starter/main.py --question "p08 项目现在是什么状态？"
```

查看参考实现：
```bash
python3 solution/main.py --question "p08 项目现在是什么状态？"
```

## 预期输出
运行 `python3 src/main.py --question "p08 项目现在是什么状态？"` 后，你会看到类似输出：

```text
连接的 server：course_ops
发现的工具：
- get_project_status：查询项目状态
- list_workshops：列出本周工作坊

选择工具：get_project_status
工具参数：{'project_key': 'p08'}
工具结果：{'project_key': 'p08', 'status': '联调中', 'owner': 'MCP 小组'}

最终回答：项目 p08 当前状态是联调中，负责人是 MCP 小组，下一步是补充接入演示。
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了“发现工具”和“调用工具”的 `TODO`
- `solution/main.py`：给出一个更短的本地接入示例
- `src/`：项目主线版本，包含更清晰的 client、session 和 agent 拆分

## 目录说明
```text
projects/p08-mcp-agent/
├── README.md
├── .env.example
├── requirements.txt
├── data/
│   ├── README.md
│   └── mcp_servers.json
├── src/
│   ├── README.md
│   ├── main.py
│   ├── mcp_agent.py
│   └── mock_mcp_server.py
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
- 能连接指定 server
- 能列出 server 提供的工具
- 能根据问题选择工具并返回结果
- 找不到 server 时会明确报错
- `python3 -m unittest discover tests` 可以通过

## 常见问题
### 1. 这和 Tool Calling 有什么区别？
Tool Calling 更像“模型决定调用哪个函数”。MCP（模型上下文协议）更强调“外部能力如何被统一发现和访问”。两者能配合，但关注点不同。

### 2. 为什么这里不用真实 MCP SDK？
因为课程目标是先看懂链路：连接、发现、调用。等这个模型建立起来，再接真实协议会更容易。

### 3. 为什么还要有 server 名称？
因为外部能力通常不是散落在本地代码里，而是来自某个独立系统或接入点。服务端（server）名称就是帮助你理解这个边界。
