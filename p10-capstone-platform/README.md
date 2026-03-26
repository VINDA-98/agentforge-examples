# p10-capstone-platform

## 项目导航速览

- 项目目标：把前面课程能力汇总成一个可演示、可扩展、可交付的毕业项目平台骨架。
- 对应章节：[第 13 章](../../docs/ch13-agent-app-interface/)、[第 14 章](../../docs/ch14-deployment-devops/)、[第 15 章](../../docs/ch15-enterprise-lowcode-cases/)、[第 16 章](../../docs/ch16-capstone/)
- 适合什么时候做：建议在完成产品化与落地阶段后统一推进，作为整套课程的最终作品与展示入口。
- 启动方式：进入目录后执行 `python3 src/main.py --mode demo --request-type faq --message "p10 项目适用于哪些章节？"`。
- GitHub 查看源码 / 下载代码：公开示例仓库项目目录，[p10-capstone-platform](https://github.com/VINDA-98/agentforge-examples/tree/main/p10-capstone-platform)
- 说明：文档站部署来自私有主仓库；网站中的下载入口统一跳到公开示例仓库。
- 返回导航：[学习路径](../../docs/learning-path.md) · [章节索引](../../docs/chapter-index.md) · [项目总览](../../docs/project-overview.md)

## 项目目标
这个项目解决“前面学到的 Agent 能力怎样收束成一个可演示、可运行、可扩展的平台骨架”这个问题。你会得到一个最小 Capstone（毕业项目）平台：它可以注册多个 Agent 服务，支持 `CLI（命令行界面）` 演示，也支持最小 `HTTP` 接口。

## 适合配套学习的章节
- 第 13 章：把 Agent（智能体）做成应用
- 第 14 章：部署、Docker（容器化运行环境）与运维
- 第 15 章：企业场景与低代码平台对比
- 第 16 章：毕业项目（Capstone）

## 适合谁
- 想把前面项目能力整合成一个“像产品”的最小骨架
- 想练习入口、服务、配置、接口边界的学员

## 项目范围
本项目会做：
- 提供一个最小平台服务层
- 注册 3 个内置 Agent：FAQ、计划生成、交付检查
- 支持命令行 `demo` 模式
- 支持标准库 HTTP 服务模式
- 提供 `starter/` 和 `solution/` 对照版本

本项目不做：
- 前端页面
- 真实数据库
- 用户登录权限系统
- 复杂部署脚本

## 项目场景
项目使用“课程 Agent 平台”场景：
- `faq`：回答课程和项目相关问题
- `plan`：给一个需求生成落地计划
- `review`：根据检查清单做交付前检查

这能帮助学员理解：毕业项目不一定一开始就要做大，而是先把平台边界跑通。

## 先解释两个入口
- `CLI（命令行界面）`：适合你本地快速演示、排错和对照输出。
- `HTTP` 接口：适合把平台当成一个服务来调用，也更接近后续部署和验收方式。

## 安装步骤
```bash
cd projects/p10-capstone-platform
cp .env.example .env
python3 -m pip install -r requirements.txt
```

## 运行命令
运行命令行演示：
```bash
python3 src/main.py --mode demo --request-type faq --message "p10 项目适用于哪些章节？"
python3 src/main.py --mode demo --request-type plan --message "我要上线一个课程答疑助手"
python3 src/main.py --mode demo --request-type review --message "请帮我检查毕业项目是否具备演示条件"
```

第一次运行建议按下面顺序做：

1. 先跑 `faq`，确认平台已经能接收请求并返回稳定结果。
2. 再跑 `plan`，观察平台如何返回更长的结构化建议。
3. 最后跑 `review`，理解平台如何把“检查”也做成一个可调用能力。

启动 HTTP 服务：
```bash
python3 src/main.py --mode serve
```

服务启动后，可以在另一个终端验证：
```bash
curl http://127.0.0.1:8787/health
curl http://127.0.0.1:8787/agents
curl -X POST http://127.0.0.1:8787/tasks \
  -H "Content-Type: application/json" \
  -d '{"request_type":"plan","message":"我要上线一个课程答疑助手"}'
```

运行测试：
```bash
python3 -m unittest discover tests
```

查看练习起点：
```bash
python3 starter/main.py --request-type faq --message "p10 项目适用于哪些章节？"
```

查看参考实现：
```bash
python3 solution/main.py --request-type faq --message "p10 项目适用于哪些章节？"
```

## 预期输出
运行 `python3 src/main.py --mode demo --request-type plan --message "我要上线一个课程答疑助手"` 后，你会看到类似输出：

```json
{
  "run_id": "run-7a3c1b2d",
  "status": "completed",
  "agent": "plan",
  "output": "建议分 3 步推进：1. 明确用户场景和输入输出；2. 做最小 CLI 或 HTTP 演示；3. 准备验收标准和演示脚本。"
}
```

三种 `request-type` 的作用也建议先记清：

| 参数值 | 作用 | 适合先拿来验证什么 |
| --- | --- | --- |
| `faq` | 回答课程和项目问题 | 平台基本路由是否正常 |
| `plan` | 输出落地计划 | 结构化结果是否清晰 |
| `review` | 给出交付检查建议 | 验收思路是否能被平台承接 |

## starter 和 solution 如何对照
- `starter/main.py`：保留了“选择 Agent”和“处理请求”的 `TODO`
- `solution/main.py`：给出一个更短的平台路由版本
- `src/`：项目主线版本，包含配置、服务、Agent 注册和 HTTP 服务

## 目录说明
```text
projects/p10-capstone-platform/
├── README.md
├── .env.example
├── requirements.txt
├── data/
│   ├── README.md
│   └── platform_catalog.json
├── src/
│   ├── README.md
│   ├── agents.py
│   ├── config.py
│   ├── main.py
│   ├── platform_service.py
│   └── server.py
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
- `demo` 模式可以处理 FAQ、计划生成和交付检查三种请求
- `serve` 模式可以启动服务并返回 JSON
- `python3 -m unittest discover tests` 可以通过
- 学员可以从这个骨架继续扩展自己的毕业项目

## 常见问题
### 1. 为什么毕业项目平台不直接做成完整 Web 产品？
因为课程这里先解决“平台边界”和“最小交付链路”。如果一开始就上完整系统，初学者会被框架和部署细节淹没。

### 2. 为什么同时提供 CLI 和 HTTP？
CLI 更适合快速演示和调试，HTTP 更适合理解“把 Agent 做成服务”的边界。两个入口都保留，学员更容易建立整体认识。

### 3. 为什么内置 Agent 只有 3 个？
毕业项目最容易失控的地方就是功能堆叠。这里故意只保留 3 个角色，帮助学员先完成一个可展示、可验收的最小平台。
