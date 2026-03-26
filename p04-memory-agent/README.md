# p04-memory-agent

## 项目概览

- 仓库定位：`agentforge-examples` 是 AgentForge 的公开示例代码仓库，服务于 AgentForge 文档站中的示例下载与配套说明。
- 当前项目：`p04-memory-agent`
- 对应文档章节：第 6 章《上下文管理与 Memory（记忆/上下文记忆）》
- 项目定位：一个围绕会话记忆与状态保存的实战示例。
- 维护说明：本项目由阿伟开发与维护。
- 阅读建议：建议配合 AgentForge 文档站对应章节阅读，再结合 `src/`、`starter/`、`solution/` 对照理解实现。
- 仓库首页：[VINDA-98/agentforge-examples](https://github.com/VINDA-98/agentforge-examples)
- 当前项目源码：[p04-memory-agent](https://github.com/VINDA-98/agentforge-examples/tree/main/p04-memory-agent)

## 如何运行（快速开始）

```bash
cd p04-memory-agent
cp .env.example .env
python -m pip install -r requirements.txt
python src/main.py --session demo --reset
python src/main.py --session demo --message "我叫阿伟"
python src/main.py --session demo --message "我想学 Tool Calling"
python src/main.py --session demo --message "你还记得我叫什么吗？"
```

可选命令：
- 运行测试：`python -m unittest discover tests`
- 运行起始代码：`python starter/main.py --message "我叫阿伟"`
- 运行参考实现：`python solution/main.py --message "我叫阿伟"`

## 项目说明
这个项目解决“Agent 怎样记住对话里的关键信息”这个问题。你会得到一个最小记忆 Agent：它把用户说过的名字和学习目标写进本地文件，下次对话时还能回忆出来。

## 适合谁
- 适合希望上手 AI Agent 开发的开发者。
- 已经理解单轮输入输出，并想继续练习多轮对话和状态保存的开发者。

## 项目范围
本项目会做：
- 把会话写入本地 JSON 文件
- 从消息中提取“名字”和“学习目标”
- 在后续对话里引用这些记忆
- 提供 `starter/` 和 `solution/` 对照版本

本项目不做：
- 向量记忆库
- 长期总结压缩
- 多用户权限系统

## 安装步骤
```bash
cd p04-memory-agent
cp .env.example .env
python -m pip install -r requirements.txt
```

## 运行命令
先清空演示会话：
```bash
python src/main.py --session demo --reset
```

再依次运行下面三条命令：
```bash
python src/main.py --session demo --message "我叫阿伟"
python src/main.py --session demo --message "我想学 Tool Calling"
python src/main.py --session demo --message "你还记得我叫什么吗？"
```

运行测试：
```bash
python -m unittest discover tests
```

查看练习起点：
```bash
python starter/main.py --message "我叫阿伟"
```

查看参考实现：
```bash
python solution/main.py --message "我叫阿伟"
```

## 预期输出
当你执行最后一条命令时，会看到类似输出：

```text
会话：demo
已记录资料：{'name': '阿伟', 'goal': 'Tool Calling'}
最近消息数：4
Agent 回复：记得，你叫阿伟。
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了“提取用户信息”和“生成回忆回复”的 `TODO`。
- `solution/main.py`：给出完整参考写法。
- `src/`：项目主线版本，适合直接运行和阅读。

## 目录说明
```text
p04-memory-agent/
├── README.md
├── .env.example
├── requirements.txt
├── data/
│   ├── README.md
│   └── sample_dialogue.txt
├── src/
│   ├── README.md
│   ├── main.py
│   ├── memory_agent.py
│   └── memory_store.py
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
- 同一个 `session` 下再次提问时，程序能回忆出之前保存的名字或目标
- 记忆内容会落到本地 JSON 文件
- `python -m unittest discover tests` 可以通过
- 能清楚看出 `starter/` 与 `solution/` 的实现差异

## 常见错误
### 1. 每次都换了新的 session
如果你第一次用 `demo`，第二次却用 `demo2`，程序当然记不住上一轮内容。

### 2. 忘了重置旧数据
如果你想重新演示，请先运行：
```bash
python src/main.py --session demo --reset
```

### 3. 误以为“记忆”一定要接数据库
本项目故意用本地 JSON 文件，目的是先看懂“保存状态”和“读取状态”的基本逻辑。
