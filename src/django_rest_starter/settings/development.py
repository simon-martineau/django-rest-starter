from .base import *

# GENERAL
# --------------------------------------------------------------------------------
DEBUG = True
SECRET_KEY = 'test_secret_key'

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append('rest_framework.authentication.SessionAuthentication')

INTERNAL_IPS = [
    '127.0.0.1',
    '172.21.0.1',
    '0.0.0.0'
]

ALLOWED_HOSTS = ['*']

STATIC_ROOT = '/var/www/static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ['POSTGRES_HOST'],
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
    }
}
