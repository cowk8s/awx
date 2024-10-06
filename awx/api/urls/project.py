
from django.urls import re_path

from awx.api.views import (
    ProjectList
)

urls = [
    re_path(r'^$', ProjectList.as_view(), name='project_list'),
]