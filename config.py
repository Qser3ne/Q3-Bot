# 配置文件示例

# WebSocket 服务配置
WS_HOST = "127.0.0.1"
WS_PORT = 8090  # WebSocket 服务运行的端口号

# 群白名单（允许机器人响应的群号）
WHITELIST_GROUPS = [
    # 123456789,  # 示例群号，请替换为实际群号
]

# 数据库配置
DATABASE_PATH = "notebook.db"

# ==================== API 配置 ====================

# 图片 API 配置
# 注意：使用第三方图片 API 时请遵守其使用条款和相关法律法规
# Lolicon API 文档：https://api.lolicon.app/#/setu
PICTURE_API_URL = "https://api.lolicon.app/setu/v2"

# 图片内容过滤级别：0=普通, 1=包含敏感内容, 2=仅敏感内容
# 建议：公开群聊使用 0，私人群聊根据需要调整
PICTURE_FILTER_LEVEL = 0  # 默认仅获取普通内容

# 随机动漫图片 API
RANDOM_PICTURE_API_URL = "https://www.dmoe.cc/random.php"

# 被屏蔽的标签列表
BLOCKED_TAGS = [
    # "示例标签",
]

# CTF 比赛信息 API
# 数据源：https://github.com/ProbiusOfficial/Hello-CTFtime
CTF_INTERNATIONAL_API_URL = "https://raw.githubusercontent.com/ProbiusOfficial/Hello-CTFtime/main/Global.json"
CTF_DOMESTIC_API_URL = ""  # 暂未实现
