import os

# Порт, который Render пробрасывает внутрь контейнера
PORT = int(os.getenv("PORT", 8443))

# MTProto секрет — только 32 hex или ee + 32 hex
SECRET = os.getenv("SECRET", "ee1234567890abcdef1234567890abcdef")

USERS = {
    "tg": SECRET
}

# Слушаем все интерфейсы
LISTEN_ADDR = "0.0.0.0"

# Режимы MTProto
MODES = {
    "classic": False,
    "secure": False,
    "tls": True
}

# Домен для TLS маскировки
TLS_DOMAIN = os.getenv("TLS_DOMAIN", "www.cloudflare.com")
