from .base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')
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
    # ...
    '127.0.0.1',
    # ...
]