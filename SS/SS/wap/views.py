# Create your views here.
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from notifications.models import Notification
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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


def inbox_view(request):
    actions = Notification.objects.filter(recipient=request.user)
    paginator = Paginator(actions, 16) # Show 16 notifications per page
    page = request.GET.get('p')

    try:
        action_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        action_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        action_list = paginator.page(paginator.num_pages)

    return render('wap/inbox.html', request, {'action_list':action_list})


def read_all_view(request):
    Notification.objects.mark_all_as_read(request.user)
    return redirect('/wap/inbox')