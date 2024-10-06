
# Python
import base64
import os
import re  # noqa
import tempfile
import socket
from datetime import timedelta

DEBUG = True
SQL_DEBUG = DEBUG

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'awx.sqlite3'),
        'ATOMIC_REQUESTS': True,
        'TEST': {
            # Test database cannot be :memory: for inventory tests.
            'NAME': os.path.join(BASE_DIR, 'awx_test.sqlite3')
        },
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Make this unique, and don't share it with anybody.
if os.path.exists('/etc/tower/SECRET_KEY'):
    with open('/etc/tower/SECRET_KEY', 'rb') as f:
        SECRET_KEY = f.read().strip()
else:
    SECRET_KEY = base64.encodebytes(os.urandom(32)).decode().rstrip()

TEMPLATES = [
    {
        'NAME': 'default',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {

        },
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ]
    },
]

ROOT_URLCONF = 'awx.urls'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'awx.api.authentication.LoggedBasicAuthentication',
    ),
}