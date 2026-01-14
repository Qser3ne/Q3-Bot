# QQ 机器人

基于 WebSocket 的 QQ 群聊机器人，支持比赛查询、事务管理、图片获取等功能。

## ⚠️ 免责声明

本项目仅供学习交流使用，请勿用于商业用途。使用本项目时请遵守相关法律法规和平台规则。

**重要提示**：
- 本机器人使用第三方 API 获取图片内容，使用者需自行承担相关风险
- 请在私人群聊或经过授权的群聊中使用
- 建议在 `config.py` 中配置白名单，限制机器人的使用范围
- 使用图片功能时请遵守相关 API 的使用条款

**使用的第三方服务**：
- [Lolicon API](https://api.lolicon.app) - 提供动漫图片搜索服务
- [dmoe.cc](https://www.dmoe.cc) - 提供随机动漫图片
- [Hello-CTFtime](https://github.com/ProbiusOfficial/Hello-CTFtime) - 提供 CTF 比赛信息

**内容安全**：
- 默认配置下仅获取普通内容
- 可通过配置文件调整内容过滤级别
- 建议在公开群聊中保持默认安全设置

## 功能特性

### 📊 比赛查询
- 查询国际 CTF 比赛信息
- 查询国内比赛信息（待完善）

### 📝 事务管理
- 添加/查询/删除主要事务
- 添加/查询/删除次要事务
- 添加/查询/删除个人事务
- 自动按时间排序

### 🖼️ 图片功能
- 随机动漫图片
- 标签搜索图片
- 支持多种内容过滤级别

## 安装部署

### 环境要求
- Python 3.12
- NapCat 或其他支持 OneBot 11 协议的 QQ 机器人框架

### 安装依赖

```bash
pip install websockets requests
```

### 配置说明
1. 编辑 `config.py` 文件：
```python
# WebSocket 服务配置
WS_HOST = "127.0.0.1"
WS_PORT = 8090

# 群白名单（填入允许机器人响应的群号）
WHITELIST_GROUPS = [
    123456789,  # 替换为实际群号
]

# 图片内容过滤级别
PICTURE_FILTER_LEVEL = 0  # 0=普通, 1=包含敏感内容, 2=仅敏感内容
```

2. 配置 NapCat 反向 WebSocket 连接：
确保与 `config.py` 中的配置一致

### 启动运行

```bash
python main.py
```

启动成功后会显示：
```
正在监听 127.0.0.1:8090
```

## 命令列表

### 帮助命令
```
/help - 显示命令帮助
```

### 比赛查询
```
/国际比赛 - 查询国际比赛
/国内比赛 - 查询国内比赛
```

### 事务管理
```
/查询事务 - 查询当前事务
/添加主要事务<内容><时间> - 添加主要事务
/添加次要事务<内容><时间> - 添加次要事务
/删除主要事务<ID> - 删除主要事务
/删除次要事务<ID> - 删除次要事务
```

示例：
```
/添加主要事务<完成项目文档><2024-12-31>
/删除主要事务<1>
```

### 个人事务（简化命令）
```
/add<内容><时间> - 添加个人事务
/query - 查询个人事务
/delete<ID> - 删除个人事务
```

### 图片功能
```
/ciallo - 获取随机动漫图片
/miao - 获取随机图片
/miao<标签> - 根据标签搜索图片
/miao2 - 获取随机特殊图片
/miao2<标签> - 根据标签搜索特殊图片
```

示例：
```
/miao<猫娘>
/miao2<风景>
```

## 项目结构

```
qq_bot/
├── main.py                # 主程序入口
├── handle.py              # 消息处理器
├── config.py              # 配置文件
├── competition/           # 比赛查询模块
├── help/                  # 帮助命令模块
├── picture/               # 普通图片模块
├── miao/                  # 图片搜索模块
└── task/                  # 事务管理模块
```

## 数据存储

项目使用 SQLite 数据库存储事务信息：
- 数据库文件：`notebook.db`（自动创建）
- 包含三张表：主要事务、次要事务、个人事务

## 开发说明

### 添加新功能模块

1. 在对应目录创建模块文件
2. 实现消息处理函数（返回 True/False 表示是否处理）
3. 在 `handle.py` 中导入并注册到路由

### 修改配置

所有配置项都在 `config.py` 中，包括：
- WebSocket 服务地址和端口
- 群白名单
- 数据库路径
- 图片过滤级别
- 标签黑名单

## 常见问题

**Q: 机器人没有响应？**
- 检查 NapCat 是否正常连接
- 确认群号是否在白名单中
- 查看控制台是否有错误信息

**Q: 数据库文件在哪里？**
- 首次运行时会在项目根目录下自动创建 `notebook.db`
- 数据库文件已在 `.gitignore` 中排除，不会提交到仓库

**Q: 如何修改监听端口？**
- 修改 `config.py` 中的 `WS_PORT`
- 同时修改 NapCat 的反向 WebSocket 配置

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

## 📚 相关文档

- [API 使用说明](API_USAGE.md) - 详细的 API 使用条款和说明
- [快速启动指南](QUICKSTART.md) - 快速上手教程

## 致谢

- [NapCat](https://github.com/NapNeko/NapCatQQ) - QQ 机器人框架
- [Lolicon API](https://api.lolicon.app) - 图片 API
- [Hello-CTFtime](https://github.com/ProbiusOfficial/Hello-CTFtime) - 比赛信息源
