from .base import *

DEBUG = False
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["symbbad.com"])

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

# Security settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True

LOGGING['handlers']['file'] = {
    'level': 'WARNING',
    'class': 'logging.FileHandler',
    'filename': r'D:\Log\Django\portfolio\logfile.log',
    'formatter': 'verbose',
}

LOGGING['loggers']['django']['handlers'].append('file')
LOGGING['loggers']['django']['level'] = 'WARNING'