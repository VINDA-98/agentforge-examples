# p01-hello-agent

## 项目导航速览

- 项目目标：做出第一个最小可运行 Agent，理解输入、配置、处理和输出的基本链路。
- 对应章节：[第 1 章](../../docs/ch01-agent-overview/)、[第 2 章](../../docs/ch02-llm-api-basics/)、[第 4 章](../../docs/ch04-python-agent-bootstrap/)
- 适合什么时候做：建议在完成第 1 到第 4 章后立刻动手，作为整套课程的第一个项目闭环。
- 启动方式：进入目录后执行 `python src/main.py --name 小李 --task "学习 Agent 基础"`。
- GitHub 查看源码 / 下载代码：公开示例仓库项目目录，[p01-hello-agent](https://github.com/VINDA-98/agentforge-examples/tree/main/p01-hello-agent)
- 说明：文档站部署来自私有主仓库；网站中的下载入口统一跳到公开示例仓库。
- 返回导航：[学习路径](../../docs/learning-path.md) · [章节索引](../../docs/chapter-index.md) · [项目总览](../../docs/project-overview.md)

## 项目目标
这个项目解决“第一个 Agent（智能体）到底长什么样”的问题。你会得到一个最小可运行的命令行 Agent：它会读取 `.env` 配置、接收用户目标，并输出一段固定格式的响应，帮助你理解“输入 -> 处理 -> 输出”这条最小主链路。

## 适合配套学习的章节
- 第 1 章：Agent（智能体）全景认知
- 第 2 章：大模型与 API（应用程序编程接口）基础
- 第 4 章：Python Agent（智能体）开发环境与第一个 Agent

## 适合谁
- 第一次接触 Agent 项目的学员
- 只会基础 Python、想先跑通一个最小项目的同学

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
cd projects/p01-hello-agent
cp .env.example .env
python -m pip install -r requirements.txt
```

本项目只使用 Python 标准库。如果你的环境已经有 Python 3.10+，上面的安装命令会很快完成。

## 运行命令
运行主线实现：
```bash
python src/main.py --name 小李 --task "学习 Agent 基础"
```

运行测试：
```bash
python -m unittest discover tests
```

查看练习起点：
```bash
python starter/main.py --name 小李 --task "学习 Agent 基础"
```

查看参考实现：
```bash
python solution/main.py --name 小李 --task "学习 Agent 基础"
```

## 预期输出
运行 `python src/main.py --name 小李 --task "学习 Agent 基础"` 后，你会看到类似输出：

```text
Agent 名称：AgentForge 小助手
用户：小李
任务：学习 Agent 基础

你好，小李！
我是 AgentForge 小助手，会用友好的方式解释 Agent 项目。
我收到的当前目标是：学习 Agent 基础。
建议先完成三步：读取输入、组合提示词、输出稳定结果。
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了核心 `TODO`，学员需要自己补全回复内容。
- `solution/main.py`：给出完整参考写法。
- `src/`：仓库主线版本，适合直接运行和阅读。

## 目录说明
```text
projects/p01-hello-agent/
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

## 验收标准
- 能成功运行 `python src/main.py`
- 输出中必须包含用户姓名和任务
- 能通过 `python -m unittest discover tests`
- 能看出 `starter/` 与 `solution/` 的实现差异

## 常见错误
### 1. 直接双击 `main.py`，看不到终端输出
请在项目目录里用命令行运行：
```bash
python src/main.py --name 小李 --task "学习 Agent 基础"
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
