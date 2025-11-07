import os

# 端口号
PORT = int(os.getenv("PORT", 8443))

# 用户列表：name -> secret（格式：tg:secret,tg2:secret2）
raw_users = os.getenv("USERS", "tg:00000000000000000000000000000001")
USERS = dict(
    entry.split(":") for entry in raw_users.split(",") if ":" in entry
)

# 模式配置，从环境变量读取布尔值
MODES = {
    "classic": os.getenv("MODE_CLASSIC", "false").lower() == "true",
    "secure":  os.getenv("MODE_SECURE", "false").lower() == "true",
    "tls":     os.getenv("MODE_TLS", "true").lower() == "true",
}

# TLS 模式下的伪装域名
TLS_DOMAIN = os.getenv("TLS_DOMAIN", "cloudflare.com")

# 广告标签，从 @MTProxybot 获取
AD_TAG = os.getenv("AD_TAG")
assert AD_TAG, "Environment variable AD_TAG must be set"
