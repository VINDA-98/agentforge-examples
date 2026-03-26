# 测试目录说明

本目录验证 `p10-capstone-platform` 的平台主流程。

## 当前覆盖
- 健康检查返回正常状态
- FAQ 请求可以得到回答
- 未知请求类型会返回错误

## 运行命令
```bash
python3 -m unittest discover tests
```
