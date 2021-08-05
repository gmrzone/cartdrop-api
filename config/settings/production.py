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
