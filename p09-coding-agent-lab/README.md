# p09-coding-agent-lab

## 项目导航速览

- 项目目标：把编码智能体的工具、护栏和评测串成一个最小工程实验闭环。
- 对应章节：[第 11 章](../../docs/ch11-coding-agents/)、[第 12 章](../../docs/ch12-evals-guardrails-observability/)
- 适合什么时候做：建议在完成第 11 和第 12 章后动手，作为工程化阶段最重要的综合实验。
- 启动方式：进入目录后执行 `python3 src/main.py analyze --file data/sample_buggy_module.py --request "请检查这个 Python 文件里的问题"`。
- GitHub 查看源码 / 下载代码：公开示例仓库项目目录，[p09-coding-agent-lab](https://github.com/VINDA-98/agentforge-examples/tree/main/p09-coding-agent-lab)
- 说明：文档站部署来自私有主仓库；网站中的下载入口统一跳到公开示例仓库。
- 返回导航：[学习路径](../../docs/learning-path.md) · [章节索引](../../docs/chapter-index.md) · [项目总览](../../docs/project-overview.md)

## 项目目标
这个项目解决“编码智能体为什么既要有工具，也要有护栏和评测”这个问题。你会得到一个最小 Coding Agent（编码智能体）实验项目：它可以读取样例代码、分析常见问题、生成修复建议，并通过最小 Eval（评测）集检查自己的输出是否稳定。

## 适合配套学习的章节
- 第 11 章：编码智能体与开发工具链
- 第 12 章：Eval（评测）、Guardrails（护栏/约束机制）、可观测性与成本优化

## 适合谁
- 想理解编码智能体不是“随便改代码”的学员
- 想练习“工具 + 护栏 + 评测”最小闭环的学员

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
项目使用“代码评审助手”场景：学员向智能体提交一个 Python 文件和一个请求，智能体先走护栏检查，再读取文件，再输出分析结果。这样更接近真实工程里的编码智能体边界。

## 安装步骤
```bash
cd projects/p09-coding-agent-lab
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
- `starter/main.py`：保留了“分析代码”和“跑评测”的 `TODO`
- `solution/main.py`：给出一个更短的编码建议器
- `src/`：项目主线版本，包含护栏、分析器和评测器

## 目录说明
```text
projects/p09-coding-agent-lab/
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

## 验收标准
- 安全请求可以正常读取和分析样例代码
- 危险请求会被护栏拦截
- `eval` 模式能给出通过率
- `python3 -m unittest discover tests` 可以通过
- 学员能看懂“工具能力”和“权限边界”为什么必须同时存在

## 常见问题
### 1. 为什么这个编码智能体不直接改文件？
因为课程这里先强调“受控分析”和“安全边界”。如果还没看懂护栏和评测，就直接让智能体改文件，教学重点会被冲淡。

### 2. 为什么评测只检查关键词？
这是最小 Eval（评测）版本。它不能代替完整质量体系，但足够帮助学员理解“要有稳定检查，而不是只看一次演示效果”。

### 3. 为什么要限制只能读取 `data/`？
真实编码智能体必须有边界。本项目用最简单的路径限制，让学员先看到“能力”与“权限”要同时设计。
