
# Python
import inspect
import logging
import time

# Django
from django.conf import settings
from django.contrib.auth import views as auth_views

# Django REST Framework
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed, ParseError, NotAcceptable, UnsupportedMediaType
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.negotiation import DefaultContentNegotiation

from rest_framework.renderers import StaticHTMLRenderer

__all__ = [
    'ListCreateAPIView',
]

class LoggedLoginView(auth_views.LoginView):
    def get(self, request, *args, **kwargs):
        # The django.auth.contrib login form doesn't perform the content
        # negotiation we've come to expect from DRF; add in code to catch
        # situations where Accept != text/html (or */*) and reply with
        # an HTTP 406
        try:
            DefaultContentNegotiation().select_renderer(request, [StaticHTMLRenderer], 'html')
        except NotAcceptable:
            resp = Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            resp.accepted_renderer = StaticHTMLRenderer()
            resp.accepted_media_type = 'text/plain'
            resp.renderer_context = {}
            return resp
        return super(LoggedLoginView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        ret = super(LoggedLoginView, self).post(request, *args, **kwargs)
        if request.user.is_authenticated:

            return ret
        else:
            # if 'username' in self.request.POST:
            ret.status_code = 401
            return ret
    
def get_default_schema():
    return views.APIView.schema
    
class APIView(views.APIView):
    schema = get_default_schema()
    
    def initialize_request(self, request, *args, **kwargs):
        """
        Store the Django REST Framework Request object as an attribute on the
        normal Django request, store time the request started.
        """
        remote_headers = ['REMOTE_ADDR', 'REMOTE_HOST']
        
        self.time_started = time.time()

        drf_request = super(APIView, self).initialize_request(request, *args, **kwargs)
        request.drf_request = drf_request
        return drf_request
    
    def finalize_response(self, request, response, *args, **kwargs):
        """
        Log warning for 400 requests.  Add header with elapsed time.
        """

        response = super(APIView, self).finalize_response(request, response, *args, **kwargs)

        return response

class GenericAPIView(generics.GenericAPIView, APIView):
    # Base class for all model-based views.

    # Subclasses should define:
    #   model = ModelClass
    #   serializer_class = SerializerClass

    def get_serializer(self, *args, **kwargs):
        serializer = super(GenericAPIView, self).get_serializer(*args, *kwargs)

        return serializer
    
    def get_queryset(self):
        if self.queryset is not None:
            return self.queryset._clone()
        elif self.model is not None:
            qs = self.model._default_manager
            # qs = optimize_queryset(qs)
            return qs
        else:
            return super(GenericAPIView, self).get_queryset()

class ListAPIView(generics.ListAPIView, GenericAPIView):
    # Base class for a read-only list view.

    def get_queryset(self):
        return self.request.user.get_queryset(self.model)
    
class ListCreateAPIView(ListAPIView, generics.ListCreateAPIView):
    def perform_create(self, serializer):
        super().perform_create(serializer)
        
class RetrieveAPIView(generics.RetrieveAPIView, GenericAPIView):
    pass