# 源码目录说明

`src/` 放项目主线实现。

## 文件说明
- `config.py`：读取环境变量，整理平台配置
- `agents.py`：定义平台内置 Agent
- `platform_service.py`：平台注册、健康检查、请求处理
- `server.py`：最小 HTTP 服务
- `main.py`：命令行入口

## 建议阅读顺序
1. 先看 `platform_service.py`
2. 再看 `agents.py`
3. 然后看 `server.py`
4. 最后运行 `main.py`
