# AgentForge Examples

English · [简体中文](README.zh-CN.md)

Ten Python labs for the AgentForge course. The sequence starts with a command-line agent, covers structured output, tools, memory, retrieval and orchestration, then brings them together in a capstone service.

Each lab has its own README, sample data, a runnable implementation under `src/`, a practice exercise under `starter/`, a reference under `solution/` and smoke tests under `tests/`.

## Run your first lab

The first lab uses only the Python standard library and runs locally with Python 3.10 or later.

```bash
git clone https://github.com/VINDA-98/agentforge-examples.git
cd agentforge-examples/p01-hello-agent
cp .env.example .env
python3 src/main.py --name Alex --task "Learn how the agent works"
python3 -m unittest discover tests
```

The program reads the input and returns a deterministic reply. After running it, try the starter exercise and compare your implementation with the reference solution.

## Labs

| Lab | Docs chapters | What to explore |
| --- | --- | --- |
| [01 · Hello agent](p01-hello-agent/) | 1, 2, 4 | Command-line inputs, configuration and a predictable response |
| [02 · Structured output](p02-structured-output-lab/) | 3 | Task cards and JSON field validation |
| [03 · Tool agent](p03-tool-agent/) | 5 | Tool selection, execution and result formatting |
| [04 · Memory agent](p04-memory-agent/) | 6 | Storing and restoring conversation context |
| [05 · RAG agent](p05-rag-agent/) | 7 | Local retrieval and handling missing evidence |
| [06 · Workflow agent](p06-workflow-agent/) | 8 | Task decomposition, state and conditional steps |
| [07 · Multi-agent team](p07-multi-agent-team/) | 9 | Assigning work to roles and coordinating their outputs |
| [08 · MCP agent](p08-mcp-agent/) | 10 | Tool discovery and invocation with a mock MCP client |
| [09 · Coding agent](p09-coding-agent-lab/) | 11, 12 | A simulated coding workflow, guardrails and evaluation |
| [10 · Capstone](p10-capstone-platform/) | 13–16 | A small service that integrates several lab concepts |

Follow the README in each lab for its inputs, expected behavior and test command.

## Author and use

The examples are developed and maintained by 阿伟. You may use them for personal learning and practice. When quoting, redistributing or adapting the examples, credit 阿伟 and link to [the original repository](https://github.com/VINDA-98/agentforge-examples).
