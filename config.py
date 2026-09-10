import os

PORT = int(os.getenv("PORT", 8443))

USERS = {
    "tg": os.getenv("SECRET", "00000000000000000000000000000001")
}

LISTEN_ADDR = "0.0.0.0"

MODES = {
    "classic": False,
    "secure": False,
    "tls": True
}

TLS_DOMAIN = os.getenv("TLS_DOMAIN", "www.cloudflare.com")
