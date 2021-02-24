import json

from .base import *
import dj_database_url

# GENERAL
# --------------------------------------------------------------------------------
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['{{cookiecutter.domain}}', ]

# APPS
# --------------------------------------------------------------------------------
INSTALLED_APPS += [
    'storages'
]

# MIDDLEWARE
# --------------------------------------------------------------------------------
MIDDLEWARE.insert(1, 'apps.core.middleware.HideAdminMiddleware')  # Insert after security middleware
# Hide admin page for certain ips

# HIDE ADMIN
# --------------------------------------------------------------------------------
HIDE_ADMIN_ALLOWED_IPS = json.loads(os.environ['DJANGO_ADMIN_WHITELIST_IPS'])

# REST FRAMEWORK
# --------------------------------------------------------------------------------
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = ['rest_framework.renderers.JSONRenderer', ]

# SECURITY
# --------------------------------------------------------------------------------
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# https://docs.djangoproject.com/en/3.1/ref/settings/#secure-proxy-ssl-header
# This tells django that requests with this header are secure (https is handled by the proxy)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# DATABASE
# --------------------------------------------------------------------------------
# parse the database url
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

# STATIC
# --------------------------------------------------------------------------------
STATIC_ROOT = 'staticfiles'  # TODO: need this?

# AWS
# --------------------------------------------------------------------------------
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
# We need this for the fonts to load
AWS_HEADERS = {
    'Access-Control-Allow-Origin': '*'
}

AWS_LOCATION = 'drs/static'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
STATICFILES_DIRS = []
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# LOGGING
# --------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}
