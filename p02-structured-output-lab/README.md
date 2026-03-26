# p02-structured-output-lab

## 项目导航速览

- 项目目标：把原始文本整理成结构化 JSON，并完成基础字段校验。
- 对应章节：[第 3 章](../../docs/ch03-prompt-structured-output/)
- 适合什么时候做：建议在完成第 3 章后立即练习，用项目把结构化输出从概念变成可运行结果。
- 启动方式：进入目录后执行 `python src/main.py --input data/sample_note.txt`。
- GitHub 查看源码 / 下载代码：公开示例仓库项目目录，[p02-structured-output-lab](https://github.com/VINDA-98/agentforge-examples/tree/main/p02-structured-output-lab)
- 说明：文档站部署来自私有主仓库；网站中的下载入口统一跳到公开示例仓库。
- 返回导航：[学习路径](../../docs/learning-path.md) · [章节索引](../../docs/chapter-index.md) · [项目总览](../../docs/project-overview.md)

## 项目目标
这个项目解决“为什么要让模型返回结构化结果”这个问题。你会把一段原始笔记整理成固定字段的 JSON，并在程序里做基础校验，理解结构化输出对后续自动处理的价值。

## 适合配套学习的章节
- 第 3 章：Prompt（提示词）工程与结构化输出

## 适合谁
- 已经能运行 Python 脚本
- 想理解 JSON 输出、字段约束和基础校验的学员

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
cd projects/p02-structured-output-lab
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
  "owner": "课程助教"
}

校验结果：通过
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了 `TODO`，你需要自己补全结构化字段。
- `solution/main.py`：给出完整参考写法。
- `src/`：项目主线版本，适合直接运行和阅读。

## 目录说明
```text
projects/p02-structured-output-lab/
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
