"""
URL configuration for awx project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include, path

from ansible_base.lib.dynamic_config.dynamic_urls import api_urls, api_version_urls, root_urls

from awx.main.views import handle_login_redirect

def get_urlpatterns(prefix=None):
    if not prefix:
        prefix = '/'
    else:
        prefix = f'/{prefix}/'
    
    urlpatterns = [
        path(f'api{prefix}', include('awx.api.urls', namespace='api')),
    ]

    urlpatterns += [
        path('', include(root_urls)),
        re_path(r'^login/', handle_login_redirect),
    ]

    try:
        import debug_toolbar

        urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]
    except ImportError:
        pass

    return urlpatterns

urlpatterns = get_urlpatterns()

