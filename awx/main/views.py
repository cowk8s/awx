
# Django
from django.http import HttpResponse, HttpResponseRedirect

def handle_login_redirect(request):
    return HttpResponseRedirect("/#/login")