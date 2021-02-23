from .base import *

# GENERAL
# --------------------------------------------------------------------------------
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['starter.simonmartineau.dev', ]

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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DATABASE_URL'],
    }
}

# STATIC
# --------------------------------------------------------------------------------
STATIC_ROOT = 'staticfiles'
