"""
WSGI config for awx project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# Prepare the AWX environment.
from awx import prepare_env, MODE

prepare_env()

import django  # NOQA
from django.conf import settings  # NOQA

from django.core.wsgi import get_wsgi_application

# Return the default Django WSGI application.
application = get_wsgi_application()
