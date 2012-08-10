# Create your views here.
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext


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
        return HttpResponse('success')
    else:
        return HttpResponse('failed')

def help_view(request):
    return render_to_response('help.html', { },
        context_instance=RequestContext(request))


def transport_view(request):
    return HttpResponse('Not impliment')


def hot_view(request):
    return HttpResponse('Not impliment')


def topic_view(request):
    return HttpResponse('Not impliment')

def source_view(request):
    return HttpResponse('Not impliment')


def home_view(request):
    return HttpResponse('Not impliment')


