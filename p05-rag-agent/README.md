# p05-rag-agent

## 项目导航速览

- 项目目标：跑通最小 RAG（检索增强生成）闭环，先检索知识再生成回答。
- 对应章节：[第 7 章](../../docs/ch07-rag-kb/)
- 适合什么时候做：建议在完成第 7 章后立即动手，用项目把知识库问答和保守回答策略练熟。
- 启动方式：进入目录后执行 `python src/main.py --question "RAG 为什么要先检索？"`。
- GitHub 查看源码 / 下载代码：公开示例仓库项目目录，[p05-rag-agent](https://github.com/VINDA-98/agentforge-examples/tree/main/p05-rag-agent)
- 说明：文档站部署来自私有主仓库；网站中的下载入口统一跳到公开示例仓库。
- 返回导航：[学习路径](../../docs/learning-path.md) · [章节索引](../../docs/chapter-index.md) · [项目总览](../../docs/project-overview.md)

## 项目目标
这个项目解决“为什么 RAG（检索增强生成）要先检索再回答”这个问题。你会得到一个最小 RAG 闭环：先从本地知识库里找相关片段，再用命中的内容拼出回答，避免凭空乱答。

## 适合配套学习的章节
- 第 7 章：RAG（检索增强生成）与知识库问答

## 适合谁
- 已经理解普通单轮问答
- 想继续练习“检索 + 回答”最小链路的学员

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
cd projects/p05-rag-agent
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
- `starter/main.py`：保留了检索和回答生成的 `TODO`
- `solution/main.py`：给出完整参考实现
- `src/`：项目主线版本，适合直接运行和阅读

## 目录说明
```text
projects/p05-rag-agent/
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
