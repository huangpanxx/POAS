# Create your views here.
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse


def login_view(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    if username and password:
        user = authenticate(username=username, password=password) 
    else:
        user = None
    if user is not None:
        logout(request) 
        login(request, user)
        return HttpResponse('ok')
    else:
        return HttpResponse('错误')

