# API 使用说明

本项目使用以下第三方 API 服务，请在使用前了解相关条款和限制。

## 📡 使用的 API 列表

### 1. Lolicon API
- **用途**：提供动漫图片搜索功能（`/miao` 系列命令）
- **官网**：https://api.lolicon.app
- **文档**：https://api.lolicon.app/#/setu
- **开源**：是（[GitHub](https://github.com/LoliCon-API/LoliCon-API)）
- **使用限制**：
  - 免费使用，有请求频率限制
  - 建议合理使用，避免频繁请求
  - 支持内容过滤参数

**合规性说明**：
- ✅ 该 API 是公开的开源项目
- ✅ 提供内容过滤选项
- ⚠️ 建议在私人群聊使用，并设置合适的过滤级别
- ⚠️ 使用者需自行承担内容风险

**配置项**：
```python
PICTURE_API_URL = "https://api.lolicon.app/setu/v2"
PICTURE_FILTER_LEVEL = 0  # 0=普通, 1=混合, 2=特殊
```

---

### 2. dmoe.cc 随机图片 API
- **用途**：提供随机动漫图片（`/ciallo` 命令）
- **网站**：https://www.dmoe.cc
- **使用限制**：免费使用

**合规性说明**：
- ✅ 公开的图片服务
- ✅ 内容相对安全
- ✅ 适合公开群聊使用

**配置项**：
```python
RANDOM_PICTURE_API_URL = "https://www.dmoe.cc/random.php"
```

---

### 3. Hello-CTFtime
- **用途**：提供 CTF 比赛信息查询（`/国际比赛` 命令）
- **GitHub**：https://github.com/ProbiusOfficial/Hello-CTFtime
- **数据源**：CTFtime.org
- **开源**：是（MIT License）

**合规性说明**：
- ✅ 完全合规的开源项目
- ✅ 数据来自公开的 CTF 比赛信息
- ✅ 可以安全使用

**配置项**：
```python
CTF_INTERNATIONAL_API_URL = "https://raw.githubusercontent.com/ProbiusOfficial/Hello-CTFtime/main/Global.json"
```

---

## 🔒 隐私与安全

### 数据收集
本机器人**不会**收集或存储以下信息：
- 用户的聊天内容（除了命令本身）
- 用户的个人信息
- 图片搜索历史

### 数据存储
本地存储的数据仅包括：
- 事务管理的任务信息（存储在本地 SQLite 数据库）
- 不会上传到任何服务器

### 第三方 API 调用
- 图片 API 调用时可能会发送搜索标签
- 建议查看各 API 的隐私政策

---

## ⚙️ 自定义 API

如果你想使用其他 API 服务，可以在 `config.py` 中修改：

### 替换图片 API
```python
# 使用其他兼容的图片 API
PICTURE_API_URL = "https://your-api.com/endpoint"
```

### 替换随机图片 API
```python
# 使用其他随机图片服务
RANDOM_PICTURE_API_URL = "https://your-random-api.com/image"
```

**注意**：替换 API 后可能需要修改对应的请求逻辑。

---

## 📋 使用建议

### 公开群聊
```python
PICTURE_FILTER_LEVEL = 0  # 仅普通内容
WHITELIST_GROUPS = [你的群号]  # 限制使用范围
```

### 私人群聊
```python
PICTURE_FILTER_LEVEL = 0  # 根据需要调整
BLOCKED_TAGS = ["不想看到的标签"]  # 自定义过滤
```

### 频率控制
建议在代码中添加请求间隔，避免频繁调用 API：
```python
import time
time.sleep(1)  # 请求间隔 1 秒
```

---

## ❓ 常见问题

**Q: 这些 API 是否合法？**
A: 是的，这些都是公开的 API 服务。但使用时需要：
- 遵守各 API 的使用条款
- 合理控制请求频率
- 注意内容合规性

**Q: 可以商用吗？**
A: 本项目仅供学习交流，不建议商用。如需商用请：
- 查看各 API 的商业使用条款
- 考虑使用付费 API 服务
- 确保符合相关法律法规

**Q: API 失效怎么办？**
A: 可以在 `config.py` 中替换为其他兼容的 API 服务。

**Q: 如何确保内容安全？**
A: 
- 使用白名单限制机器人使用范围
- 设置合适的过滤级别
- 添加标签黑名单
- 定期检查使用情况

---

## 📞 联系与反馈

如果你发现 API 使用方面的问题或有改进建议，欢迎提交 Issue。
