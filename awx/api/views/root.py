
from collections import OrderedDict

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.translation import gettext_lazy as _

from rest_framework.response import Response

from awx.api.generics import APIView

class ApiRootView(APIView):
    name = _('REST API')

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, format=None):
        data = OrderedDict()
        return Response(data)