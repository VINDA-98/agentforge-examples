# p03-tool-agent

## 项目导航速览

- 项目目标：让 Agent 根据用户请求选择工具、执行工具并整理结果。
- 对应章节：[第 5 章](../../docs/ch05-tool-calling/)
- 适合什么时候做：建议在完成第 5 章后动手，作为 Tool Calling（工具调用）能力的第一轮实战。
- 启动方式：进入目录后执行 `python src/main.py --query "请计算 12 + 30"`。
- GitHub 查看源码 / 下载代码：公开示例仓库项目目录，[p03-tool-agent](https://github.com/VINDA-98/agentforge-examples/tree/main/p03-tool-agent)
- 说明：文档站部署来自私有主仓库；网站中的下载入口统一跳到公开示例仓库。
- 返回导航：[学习路径](../../docs/learning-path.md) · [章节索引](../../docs/chapter-index.md) · [项目总览](../../docs/project-overview.md)

## 项目目标
这个项目解决“Agent 怎么决定要不要调用工具”这个问题。你会得到一个最小 Tool Calling（工具调用）示例：程序先根据用户问题选择工具，再执行工具函数，最后把工具结果整理成回答。

## 适合配套学习的章节
- 第 5 章：Tool Calling（工具调用）与函数调用

## 适合谁
- 已经能写基础 Python 函数
- 想把“函数调用”升级为“Agent 选择并使用工具”的学员

## 项目范围
本项目会做：
- 提供两个最小工具：加法计算、课程问答查询
- 根据用户输入自动选择工具
- 执行工具并返回结果
- 提供 `starter/` 和 `solution/` 对照版本

本项目不做：
- 真实模型函数调用协议
- 外部 API 接入
- 多轮记忆

## 安装步骤
```bash
cd projects/p03-tool-agent
cp .env.example .env
python -m pip install -r requirements.txt
```

## 运行命令
运行主线实现：
```bash
python src/main.py --query "请计算 12 + 30"
python src/main.py --query "什么是 Tool Calling"
```

运行测试：
```bash
python -m unittest discover tests
```

查看练习起点：
```bash
python starter/main.py --query "请计算 12 + 30"
```

查看参考实现：
```bash
python solution/main.py --query "请计算 12 + 30"
```

## 预期输出
运行 `python src/main.py --query "请计算 12 + 30"` 后，你会看到类似输出：

```text
选择工具：calculator
工具输入：{'a': 12.0, 'b': 30.0}
工具结果：42.0
最终回答：我调用了 calculator，计算结果是 42.0。
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了工具选择和结果拼装的 `TODO`
- `solution/main.py`：给出完整参考实现
- `src/`：项目主线版本，适合直接运行和阅读

## 目录说明
```text
projects/p03-tool-agent/
├── README.md
├── .env.example
├── requirements.txt
├── data/
│   ├── README.md
│   └── course_faq.json
├── src/
│   ├── README.md
│   ├── main.py
│   ├── tool_agent.py
│   └── tools.py
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
- 能正确识别计算题并调用加法工具
- 能正确识别课程概念题并调用问答工具
- `python -m unittest discover tests` 可以通过
- 能看出 `starter/` 和 `solution/` 的实现差异

## 常见错误
### 1. 误以为“工具调用”就是直接 `if/else`
`if/else` 是最小版本的决策逻辑。本项目故意把“选择工具”和“执行工具”拆开，帮助你理解 Tool Calling 链路。

### 2. 让计算工具支持太多表达式
本项目只支持两个数字的加法，目的是把重点放在调用链路，而不是解析复杂语法。

### 3. FAQ 文件路径写错
如果你改了数据文件路径，请同步更新命令参数或 `.env`。
