# p04-memory-agent

## 项目导航速览

- 项目目标：实现最小会话记忆，让 Agent 记住名字、目标和最近上下文。
- 对应章节：[第 6 章](../../docs/ch06-memory-context/)
- 适合什么时候做：建议在完成第 6 章后边学边做，用项目验证多轮对话与状态保存是否真正理解。
- 启动方式：进入目录后先执行 `python src/main.py --session demo --reset`，再按 README 中的多轮消息示例继续。
- GitHub 查看源码 / 下载代码：公开示例仓库项目目录，[p04-memory-agent](https://github.com/VINDA-98/agentforge-examples/tree/main/p04-memory-agent)
- 说明：文档站部署来自私有主仓库；网站中的下载入口统一跳到公开示例仓库。
- 返回导航：[学习路径](../../docs/learning-path.md) · [章节索引](../../docs/chapter-index.md) · [项目总览](../../docs/project-overview.md)

## 项目目标
这个项目解决“Agent 怎样记住对话里的关键信息”这个问题。你会得到一个最小记忆 Agent：它把用户说过的名字和学习目标写进本地文件，下次对话时还能回忆出来。

## 适合配套学习的章节
- 第 6 章：上下文管理与 Memory（记忆/上下文记忆）

## 适合谁
- 已经理解单轮输入输出
- 想继续练习多轮对话和状态保存的学员

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
cd projects/p04-memory-agent
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
python src/main.py --session demo --message "我叫小王"
python src/main.py --session demo --message "我想学 Tool Calling"
python src/main.py --session demo --message "你还记得我叫什么吗？"
```

运行测试：
```bash
python -m unittest discover tests
```

查看练习起点：
```bash
python starter/main.py --message "我叫小王"
```

查看参考实现：
```bash
python solution/main.py --message "我叫小王"
```

## 预期输出
当你执行最后一条命令时，会看到类似输出：

```text
会话：demo
已记录资料：{'name': '小王', 'goal': 'Tool Calling'}
最近消息数：4
Agent 回复：记得，你叫小王。
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了“提取用户信息”和“生成回忆回复”的 `TODO`
- `solution/main.py`：给出完整参考写法
- `src/`：项目主线版本，适合直接运行和阅读

## 目录说明
```text
projects/p04-memory-agent/
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
