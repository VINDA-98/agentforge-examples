# p09-coding-agent-lab

## 项目概览

- 仓库定位：`agentforge-examples` 是 AgentForge 的公开示例代码仓库，服务于 AgentForge 文档站中的示例下载与配套说明。
- 当前项目：`p09-coding-agent-lab`
- 对应文档章节：第 11 章《编码智能体与开发工具链》、第 12 章《Eval（评测）、Guardrails（护栏/约束机制）、可观测性与成本优化》
- 项目定位：一个围绕工具、护栏与评测闭环的 Coding Agent 实战示例。
- 维护说明：本项目由阿伟开发与维护。
- 阅读建议：建议配合 AgentForge 文档站对应章节阅读，再结合 `src/`、`starter/`、`solution/` 对照理解实现。
- 仓库首页：[VINDA-98/agentforge-examples](https://github.com/VINDA-98/agentforge-examples)
- 当前项目源码：[p09-coding-agent-lab](https://github.com/VINDA-98/agentforge-examples/tree/main/p09-coding-agent-lab)

## 如何运行（快速开始）

```bash
cd p09-coding-agent-lab
cp .env.example .env
python3 -m pip install -r requirements.txt
python3 src/main.py analyze --file data/sample_buggy_module.py --request "请检查这个 Python 文件里的问题"
```

可选命令：
- 运行评测：`python3 src/main.py eval`
- 运行测试：`python3 -m unittest discover tests`
- 运行起始代码：`python3 starter/main.py analyze --file data/sample_buggy_module.py --request "请检查这个 Python 文件里的问题"`
- 运行参考实现：`python3 solution/main.py --request "请检查这个 Python 文件里的问题"`

## 项目说明
这个项目解决“编码智能体为什么既要有工具，也要有护栏和评测”这个问题。你会得到一个最小 Coding Agent（编码智能体）实验项目：它可以读取样例代码、分析常见问题、生成修复建议，并通过最小 Eval（评测）集检查自己的输出是否稳定。

## 适合谁
- 适合希望上手 AI Agent 开发的开发者。
- 想理解编码智能体不是“随便改代码”，并想练习“工具 + 护栏 + 评测”最小闭环的开发者。

## 项目范围
本项目会做：
- 读取一个允许范围内的代码文件
- 分析调试输出、异常吞掉、除零风险等常见问题
- 生成结构化修复建议
- 拦截危险请求和越界文件读取
- 运行最小评测集
- 提供 `starter/` 和 `solution/` 对照版本

本项目不做：
- 自动改写整个仓库
- 任意执行 shell 命令
- 真实大模型推理
- 复杂沙箱系统

## 项目场景
项目使用“代码评审助手”场景：开发者向智能体提交一个 Python 文件和一个请求，智能体先走护栏检查，再读取文件，再输出分析结果。这样更接近真实工程里的编码智能体边界。

## 安装步骤
```bash
cd p09-coding-agent-lab
cp .env.example .env
python3 -m pip install -r requirements.txt
```

## 运行命令
运行代码分析：
```bash
python3 src/main.py analyze --file data/sample_buggy_module.py --request "请检查这个 Python 文件里的问题"
```

运行评测：
```bash
python3 src/main.py eval
```

运行测试：
```bash
python3 -m unittest discover tests
```

查看练习起点：
```bash
python3 starter/main.py analyze --file data/sample_buggy_module.py --request "请检查这个 Python 文件里的问题"
```

查看参考实现：
```bash
python3 solution/main.py --request "请检查这个 Python 文件里的问题"
```

## 预期输出
运行分析命令后，你会看到类似输出：

```text
护栏状态：通过
分析总结：发现 3 个需要优先处理的问题。
发现的问题：
1. 检测到调试输出 print(...)，建议在提交前移除。
2. 检测到直接除法，建议补充零值检查。
3. 检测到 except Exception 后直接 pass，容易吞掉错误。

修复建议：
1. 删除或替换调试输出为正式日志。
2. 在除法前增加 if b == 0 的保护分支。
3. 不要直接 pass，至少返回明确错误或重新抛出异常。
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了“分析代码”和“跑评测”的 `TODO`。
- `solution/main.py`：给出一个更短的编码建议器。
- `src/`：项目主线版本，包含护栏、分析器和评测器。

## 目录说明
```text
p09-coding-agent-lab/
├── README.md
├── .env.example
├── requirements.txt
├── data/
│   ├── README.md
│   ├── eval_cases.json
│   └── sample_buggy_module.py
├── src/
│   ├── README.md
│   ├── coding_agent.py
│   ├── eval_runner.py
│   ├── guardrails.py
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
- 安全请求可以正常读取和分析样例代码
- 危险请求会被护栏拦截
- `eval` 模式能给出通过率
- `python3 -m unittest discover tests` 可以通过
- 开发者能看懂“工具能力”和“权限边界”为什么必须同时存在

## 常见问题
### 1. 为什么这个编码智能体不直接改文件？
因为这里先强调“受控分析”和“安全边界”。如果还没看懂护栏和评测，就直接让智能体改文件，重点会被冲淡。

### 2. 为什么评测只检查关键词？
这是最小 Eval（评测）版本。它不能代替完整质量体系，但足够帮助开发者理解“要有稳定检查，而不是只看一次演示效果”。

### 3. 为什么要限制只能读取 `data/`？
真实编码智能体必须有边界。本项目用最简单的路径限制，让开发者先看到“能力”与“权限”要同时设计。
