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
    '127.0.0.1',
    # ...
]