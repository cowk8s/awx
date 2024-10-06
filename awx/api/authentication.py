# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

# Python
import logging

# Django
from django.conf import settings
from django.utils.encoding import smart_str

# Django REST Framework
from rest_framework import authentication

# Django-OAuth-Toolkit
# from oauth2_provider.contrib.rest_framework import OAuth2Authentication

logger = logging.getLogger('awx.api.authentication')

class LoggedBasicAuthentication(authentication.BasicAuthentication):
    def authenticate(self, request):
        ret = super(LoggedBasicAuthentication, self).authenticate(request)
        if ret:
            username = ret[0].username if ret[0] else '<none>'
            
        return ret