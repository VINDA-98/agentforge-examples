# p02-structured-output-lab

## 项目概览

- 仓库定位：`agentforge-examples` 是 AgentForge 的公开示例代码仓库，服务于 AgentForge 文档站中的示例下载与配套说明。
- 当前项目：`p02-structured-output-lab`
- 对应文档章节：第 3 章《Prompt（提示词）工程与结构化输出》
- 项目定位：一个围绕结构化输出与字段校验的实战示例。
- 维护说明：本项目由阿伟开发与维护。
- 阅读建议：建议配合 AgentForge 文档站对应章节阅读，再结合 `src/`、`starter/`、`solution/` 对照理解实现。
- 仓库首页：[VINDA-98/agentforge-examples](https://github.com/VINDA-98/agentforge-examples)
- 当前项目源码：[p02-structured-output-lab](https://github.com/VINDA-98/agentforge-examples/tree/main/p02-structured-output-lab)

## 如何运行（快速开始）

```bash
cd p02-structured-output-lab
cp .env.example .env
python -m pip install -r requirements.txt
python src/main.py --input data/sample_note.txt
```

可选命令：
- 运行测试：`python -m unittest discover tests`
- 运行起始代码：`python starter/main.py --input data/sample_note.txt`
- 运行参考实现：`python solution/main.py --input data/sample_note.txt`

## 项目说明
这个项目解决“为什么要让模型返回结构化结果”这个问题。你会把一段原始笔记整理成固定字段的 JSON，并在程序里做基础校验，理解结构化输出对后续自动处理的价值。

## 适合谁
- 适合希望上手 AI Agent 开发的开发者。
- 已经能运行 Python 脚本，并想理解 JSON 输出、字段约束和基础校验的开发者。

## 项目范围
本项目会做：
- 读取一段原始文本笔记
- 生成固定结构的任务卡片
- 校验字段是否完整、类型是否正确
- 提供 `starter/` 和 `solution/` 对照版本

本项目不做：
- 真实线上模型调用
- 复杂表单系统
- 长链路工作流

## 安装步骤
```bash
cd p02-structured-output-lab
cp .env.example .env
python -m pip install -r requirements.txt
```

## 运行命令
运行主线实现：
```bash
python src/main.py --input data/sample_note.txt
```

运行测试：
```bash
python -m unittest discover tests
```

查看练习起点：
```bash
python starter/main.py --input data/sample_note.txt
```

查看参考实现：
```bash
python solution/main.py --input data/sample_note.txt
```

## 预期输出
运行 `python src/main.py --input data/sample_note.txt` 后，你会看到类似输出：

```text
结构化结果：
{
  "title": "修复登录页报错",
  "summary": "从原始笔记中整理出一张最小任务卡片。",
  "action_items": [
    "修复登录页报错",
    "补充接口文档",
    "周五前发测试包"
  ],
  "priority": "高",
  "owner": "阿伟"
}

校验结果：通过
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了 `TODO`，开发者可以在这里补全结构化字段。
- `solution/main.py`：给出完整参考写法。
- `src/`：项目主线版本，适合直接运行和阅读。

## 目录说明
```text
p02-structured-output-lab/
├── README.md
├── .env.example
├── requirements.txt
├── data/
│   ├── README.md
│   ├── invalid_card.json
│   └── sample_note.txt
├── src/
│   ├── README.md
│   ├── main.py
│   └── structured_output.py
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
- `python src/main.py --input data/sample_note.txt` 能输出 JSON
- 输出结构必须包含 `title`、`summary`、`action_items`、`priority`、`owner`
- `python -m unittest discover tests` 可以通过
- 能清楚看出 `starter/` 与 `solution/` 的差异

## 常见错误
### 1. 输入文件路径写错
请在项目目录内运行，或传入正确的相对路径：
```bash
python src/main.py --input data/sample_note.txt
```

### 2. 把 Python 字典当成 JSON
JSON 里的键名必须带双引号。本项目使用 `json.dumps()` 输出，避免手写格式。

### 3. 忘了做字段校验
结构化输出不只是“长得像 JSON”，还要验证字段完整性。这个项目的 `validate_task_card()` 就是最小例子。
