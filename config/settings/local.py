from datetime import timedelta

from .base import *

DEBUG = True

INSTALLED_APPS.append("debug_toolbar")

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE


ALLOWED_HOSTS = ["*"]
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


CORS_ALLOW_ALL_ORIGINS = True

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=4),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    # Http Only Cookie
    "AUTH_COOKIE": "access_token",  # Cookie name. Enables cookies if value is set.
    "AUTH_COOKIE_REFRESH": "refresh_token",  # refresh Cookie name. Enables cookies if value is set.
    "AUTH_COOKIE_DOMAIN": None,  # A string like "example.com", or None for standard domain cookie.
    "AUTH_COOKIE_SECURE": False,  # Whether the auth cookies should be secure (https:// only).
    "AUTH_COOKIE_HTTP_ONLY": True,  # Http only cookie flag.It's not fetch by javascript.
    "AUTH_COOKIE_PATH": "/",  # The path of the auth cookie.
    "AUTH_COOKIE_SAMESITE": "Lax",  # Whether to set the flag restricting cookie leaks on cross-site requests.
    # This can be 'Lax', 'Strict', or None to disable the flag.
}
