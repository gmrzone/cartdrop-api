
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": get_value('CARTDROP_DEV_DB_NAME'),
        "USER": get_value('CARTDROP_DEV_DB_USER'),
        "PASSWORD": get_value('CARTDROP_DEV_DB_PASSWORD'),
        "HOST": get_value('CARTDROP_DEV_DB_HOST'),
        "PORT": "5432",
    }
}