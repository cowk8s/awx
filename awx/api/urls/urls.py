

from django.urls import include, re_path

from awx.api.generics import LoggedLoginView
from awx.api.views.root import (
    ApiRootView
)

from .project import urls as project_urls

v2_urls = [
    re_path(r'^projects/', include(project_urls)),  
]

app_name = 'api'
urlpatterns = [
    re_path(r'^$', ApiRootView.as_view(), name='api_root_view'),
    re_path(r'^(?P<version>(v2))/', include(v2_urls)),
    re_path(r'^login/$', LoggedLoginView.as_view(template_name='rest_framework/login.html', extra_context={'inside_login_context': True}), name='login'),
]