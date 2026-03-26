# p05-rag-agent

## 项目概览

- 仓库定位：`agentforge-examples` 是 AgentForge 的公开示例代码仓库，服务于 AgentForge 文档站中的示例下载与配套说明。
- 当前项目：`p05-rag-agent`
- 对应文档章节：第 7 章《RAG（检索增强生成）与知识库问答》
- 项目定位：一个围绕本地检索与保守回答的 RAG 实战示例。
- 维护说明：本项目由阿伟开发与维护。
- 阅读建议：建议配合 AgentForge 文档站对应章节阅读，再结合 `src/`、`starter/`、`solution/` 对照理解实现。
- 仓库首页：[VINDA-98/agentforge-examples](https://github.com/VINDA-98/agentforge-examples)
- 当前项目源码：[p05-rag-agent](https://github.com/VINDA-98/agentforge-examples/tree/main/p05-rag-agent)

## 如何运行（快速开始）

```bash
cd p05-rag-agent
cp .env.example .env
python -m pip install -r requirements.txt
python src/main.py --question "RAG 为什么要先检索？"
```

可选命令：
- 运行测试：`python -m unittest discover tests`
- 运行起始代码：`python starter/main.py --question "RAG 为什么要先检索？"`
- 运行参考实现：`python solution/main.py --question "RAG 为什么要先检索？"`

## 项目说明
这个项目解决“为什么 RAG（检索增强生成）要先检索再回答”这个问题。你会得到一个最小 RAG 闭环：先从本地知识库里找相关片段，再用命中的内容拼出回答，避免凭空乱答。

## 适合谁
- 适合希望上手 AI Agent 开发的开发者。
- 已经理解普通单轮问答，并想继续练习“检索 + 回答”最小链路的开发者。

## 项目范围
本项目会做：
- 读取本地知识库
- 把文档切成更小的片段
- 根据问题做最小相关性检索
- 用检索结果生成回答
- 提供 `starter/` 和 `solution/` 对照版本

本项目不做：
- 向量数据库
- 真实 Embedding（向量表示）模型
- 复杂排序器

## 安装步骤
```bash
cd p05-rag-agent
cp .env.example .env
python -m pip install -r requirements.txt
```

## 运行命令
运行主线实现：
```bash
python src/main.py --question "RAG 为什么要先检索？"
python src/main.py --question "第 5 章讲什么？"
```

运行测试：
```bash
python -m unittest discover tests
```

查看练习起点：
```bash
python starter/main.py --question "RAG 为什么要先检索？"
```

查看参考实现：
```bash
python solution/main.py --question "RAG 为什么要先检索？"
```

## 预期输出
运行 `python src/main.py --question "RAG 为什么要先检索？"` 后，你会看到类似输出：

```text
命中片段：
1. [第 7 章：RAG] RAG 会先检索知识，再把检索到的内容交给生成步骤。

最终回答：根据《第 7 章：RAG》，RAG 会先检索知识，再把检索到的内容交给生成步骤。
```

## starter 和 solution 如何对照
- `starter/main.py`：保留了检索和回答生成的 `TODO`。
- `solution/main.py`：给出完整参考实现。
- `src/`：项目主线版本，适合直接运行和阅读。

## 目录说明
```text
p05-rag-agent/
├── README.md
├── .env.example
├── requirements.txt
├── data/
│   ├── README.md
│   └── knowledge_base.json
├── src/
│   ├── README.md
│   ├── main.py
│   ├── rag_agent.py
│   └── retriever.py
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
- 能根据问题命中相关知识片段
- 命中时回答必须引用知识库内容
- 未命中时能明确说“没有找到”
- `python -m unittest discover tests` 可以通过

## 常见错误
### 1. 把 RAG 理解成“直接把文档拼给模型”
真正关键是先检索，再只用相关内容回答。本项目虽然很小，但已经把这两步拆开了。

### 2. 没有处理未命中场景
如果问题和知识库完全无关，程序应该明确提示“没找到”，而不是随便编答案。

### 3. 检索规则写得过于复杂
这是入门项目，重点是看懂流程，不是追求召回率最优。
