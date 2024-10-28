# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

# Python
import contextlib
import logging
import threading
import json
import sys

# Django
from django.db import connection
from django.conf import settings

class ActivityStreamEnabled(threading.local):
    def __init__(self):
        self.enabled = True

    def __bool__(self):
        return bool(self.enabled and getattr(settings, 'ACTIVITY_STREAM_ENABLED', True))

activity_stream_enabled = ActivityStreamEnabled()

@contextlib.contextmanager
def disable_activity_stream():
    """
    Context manager to disable capturing activity stream changes.
    """
    try:
        previous_value = activity_stream_enabled.enabled
        activity_stream_enabled.enabled = False
        yield
    finally:
        activity_stream_enabled.enabled = previous_value
