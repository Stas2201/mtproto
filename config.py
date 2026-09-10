import os

# Читаем порт из Render
PORT = int(os.getenv("PORT", 8443))

# Читаем секрет из Render
USERS = {
    "tg": os.getenv("SECRET", "00000000000000000000000000000001")
}

# Прокси должен слушать весь интернет, иначе Render не увидит порт
LISTEN_ADDR = "0.0.0.0"

MODES = {
    "classic": False,
    "secure": False,
    "tls": True
}

# Домен для TLS
TLS_DOMAIN = os.getenv("TLS_DOMAIN", "www.cloudflare.com")
