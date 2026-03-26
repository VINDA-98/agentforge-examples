# p01-hello-agent

## 项目概览

- 仓库定位：`agentforge-examples` 是 AgentForge 的公开示例代码仓库，服务于 AgentForge 文档站中的示例下载与配套说明。
- 当前项目：`p01-hello-agent`
- 对应文档章节：第 1 章《Agent（智能体）全景认知》、第 2 章《大模型与 API（应用程序编程接口）基础》、第 4 章《Python Agent（智能体）开发环境与第一个 Agent》
- 项目定位：一个最小可运行的 Hello Agent 实战示例。
- 维护说明：本项目由阿伟开发与维护。
- 阅读建议：建议配合 AgentForge 文档站对应章节阅读，再结合 `src/`、`starter/`、`solution/` 对照理解实现。
- 仓库首页：[VINDA-98/agentforge-examples](https://github.com/VINDA-98/agentforge-examples)
- 当前项目源码：[p01-hello-agent](https://github.com/VINDA-98/agentforge-examples/tree/main/p01-hello-agent)

## 如何运行（快速开始）

```bash
cd p01-hello-agent
cp .env.example .env
python -m pip install -r requirements.txt
python src/main.py --name 阿伟 --task "学习 Agent 基础"
```

可选命令：
- 运行测试：`python -m unittest discover tests`
- 运行起始代码：`python starter/main.py --name 阿伟 --task "学习 Agent 基础"`
- 运行参考实现：`python solution/main.py --name 阿伟 --task "学习 Agent 基础"`

## 项目说明
这个项目解决“第一个 Agent 到底长什么样”这个问题。你会得到一个最小可运行的命令行 Agent：它会读取 `.env` 配置、接收用户目标，并输出一段固定格式的响应，帮助你理解“输入 -> 处理 -> 输出”这条最小主链路。

## 适合谁
- 适合希望上手 AI Agent 开发的开发者。
- 想先跑通一个最小命令行 Agent，再理解输入、处理、输出闭环的开发者。

## 项目范围
本项目会做：
- 读取 `.env` 中的基础配置
- 用命令行参数接收姓名和任务
- 生成一段稳定、可验证的 Agent 回复
- 提供 `starter/` 和 `solution/` 对照版本

本项目不做：
- 真实线上模型调用
- 多轮对话
- Tool Calling（工具调用）
- Web 页面

## 安装步骤
```bash
cd p01-hello-agent
cp .env.example .env
python -m pip install -r requirements.txt
```

本项目只使用 Python 标准库。如果你的环境已经有 Python 3.10+，上面的安装命令会很快完成。

## 运行命令
运行主线实现：
```bash
python src/main.py --name 阿伟 --task "学习 Agent 基础"
```

运行测试：
```bash
python -m unittest discover tests
```

查看练习起点：
```bash
python starter/main.py --name 阿伟 --task "学习 Agent 基础"
```

查看参考实现：
```bash
python solution/main.py --name 阿伟 --task "学习 Agent 基础"
```

## 预期输出
运行 `python src/main.py --name 阿伟 --task "学习 Agent 基础"` 后，你会看到类似输出：

```text
Agent 名称：AgentForge 小助手
用户：阿伟
任务：学习 Agent 基础

你好，阿伟！
我是 AgentForge 小助手，会用简洁的方式解释 Agent 项目。
我收到的当前目标是：学习 Agent 基础。
建议先完成三步：读取输入、组合提示词、输出稳定结果。
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了核心 `TODO`，开发者可以在这里补全回复内容。
- `solution/main.py`：给出完整参考写法。
- `src/`：仓库主线版本，适合直接运行和阅读。

## 目录说明
```text
p01-hello-agent/
├── README.md
├── .env.example
├── requirements.txt
├── data/
│   ├── README.md
│   └── sample_task.txt
├── src/
│   ├── README.md
│   ├── config.py
│   ├── hello_agent.py
│   └── main.py
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
- 能成功运行 `python src/main.py`
- 输出中必须包含用户姓名和任务
- 能通过 `python -m unittest discover tests`
- 能看出 `starter/` 与 `solution/` 的实现差异

## 常见错误
### 1. 直接双击 `main.py`，看不到终端输出
请在项目目录里用命令行运行：
```bash
python src/main.py --name 阿伟 --task "学习 Agent 基础"
```

### 2. 使用了错误的 Python 版本
如果你看到语法或类型报错，先检查版本：
```bash
python --version
```

### 3. 忘了复制 `.env.example`
虽然本项目有默认值，但建议先执行：
```bash
cp .env.example .env
```
这样更容易理解环境变量在 Agent 项目中的作用。
