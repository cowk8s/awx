
from __future__ import absolute_import, unicode_literals

import os
import sys

MODE = 'development'

def prepare_env():
    # Update the default settings environment variable based on current mode.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'awx.settings.%s' % MODE)

def manage():
    # Prepare the AWX environment.
    prepare_env()
    # Now run the command (or display the version).
    from django.conf import settings
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

