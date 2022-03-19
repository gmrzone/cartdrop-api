from datetime import timedelta

from .base import *

DEBUG = False

ALLOWED_HOSTS = ["cartdrop.afzalsaiyed.info", "www.cartdrop.afzalsaiyed.info"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "5432",
    }
}

ADMINS = (
    ("Afzal", "saiyedafzalgz@gmail.com"),
    ("afzal1", "saiyedafzalaz@gmail.com"),
    ("Samar", "dalvisamar333@gmail.com"),
)

# # # HTTPS Settings
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# # # HSTS SETTINGS
# SECURE_HSTS_SECONDS = 31536000 # 1 year
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = ["https://cartdrop.afzalsaiyed.info", "https://cartdrop.info"]

# LOGGING

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "loggers": {"django": {"handlers": ["file"], "level": "DEBUG"}},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": f"{BASE_DIR}/logs/main.log",
            "formatter": "cart_drop_formatter",
        }
    },
    "formatters": {
        "cart_drop_formatter": {
            "format": "{asctime} {levelname} {name} {message}",
            "style": "{",
        }
    },
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=4),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    # Http Only Cookie
    "AUTH_COOKIE": "access_token",  # Cookie name. Enables cookies if value is set.
    "AUTH_COOKIE_REFRESH": "refresh_token",  # refresh Cookie name. Enables cookies if value is set.
    "AUTH_COOKIE_DOMAIN": None,  # A string like "example.com", or None for standard domain cookie.
    "AUTH_COOKIE_SECURE": True,  # Whether the auth cookies should be secure (https:// only).
    "AUTH_COOKIE_HTTP_ONLY": True,  # Http only cookie flag.It's not fetch by javascript.
    "AUTH_COOKIE_PATH": "/",  # The path of the auth cookie.
    "AUTH_COOKIE_SAMESITE": "Lax",  # Whether to set the flag restricting cookie leaks on cross-site requests.
    # This can be 'Lax', 'Strict', or None to disable the flag.
}
