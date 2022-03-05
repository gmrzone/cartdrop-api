from datetime import timedelta

from .base import *

DEBUG = True

INSTALLED_APPS.append("debug_toolbar")

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": get_value("CARTDROP_DEV_DB_NAME"),
        "USER": get_value("POSTGRES_USER"),
        "PASSWORD": get_value("POSTGRES_PASSWORD"),
        "HOST": get_value("CARTDROP_DEV_DB_HOST"),
        "PORT": "5432",
    }
}


CORS_ALLOW_ALL_ORIGINS = True


INTERNAL_IPS = [
    "127.0.0.1",
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
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
