# Create your views here.
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def render(html_path, request, dic_data):
    return render_to_response(html_path, dic_data,
        context_instance=RequestContext(request))


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
    return render('wap/help.html', request, {})

def transport_view(request):
    return render('wap/transport.html', request, {})


def hot_view(request):
    return render('wap/hot.html', request, {})


def topic_view(request):
    return render('wap/topic.html', request, {})

def source_view(request):
    return render('wap/source.html', request, {})


def home_view(request):
    return HttpResponseRedirect('./hot/')


