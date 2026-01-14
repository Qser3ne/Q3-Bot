# 快速启动指南

## 首次使用

### 1. 安装依赖
```bash
pip install websockets requests
```

### 2. 配置机器人

编辑 `config.py`，填入你的群号：
```python
WHITELIST_GROUPS = [
    123456789,  # 替换为你的群号
]
```

### 3. 配置 NapCat

在 NapCat 中添加反向 WebSocket 配置：
- 地址：`ws://127.0.0.1:8090`
- 确保端口与 `config.py` 中的 `WS_PORT` 一致

### 4. 启动机器人

```bash
cd Bot
python main.py
```

看到 `正在监听 127.0.0.1:8090` 表示启动成功。

### 5. 测试

在群聊中发送 `/help` 查看命令列表。

## 常用配置

### 修改监听端口
```python
WS_PORT = 8090  # 改为其他端口
```

### 设置图片过滤级别
```python
PICTURE_FILTER_LEVEL = 0  # 0=普通, 1=混合, 2=特殊
```

### 添加标签黑名单
```python
BLOCKED_TAGS = [
    "不想看到的标签",
]
```

## 故障排查

### 机器人无响应
1. 检查 NapCat 是否显示 "napcat 已连接"
2. 确认群号在 `WHITELIST_GROUPS` 中
3. 查看控制台是否有错误信息

### 导入错误
确保在 `Bot/` 目录下运行：
```bash
cd Bot
python main.py
```

### 数据库错误
删除 `notebook.db` 文件，重新启动会自动创建。

## 进阶使用

查看完整文档：[README.md](README.md)
