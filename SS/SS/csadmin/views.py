# Create your views here.
#coding:utf8
from .models import settings
from django.http import HttpResponse
from .utils import jsonrpc_call_server
from django.template.loader import get_template
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
from csadmin.utils import json_get_server

def address(request):
    notices = []
    if request.method == "POST":
        server_address = request.POST.get('server_address','')
        server_port    = request.POST.get('server_port','')
        spider_port    = request.POST.get('spider_port','')
        # validate
        if not server_address:
            notices.append('Server Address is Missing')
        else:
            pass
        if not server_port:
            notices.append('Server Port is Missing')
        else:
            pass
        if not spider_port:
            notices.append('Spider Port is Missing')
        else:
            pass
        
        # update
        if not notices:
            try:
                settings.server_address = server_address
                settings.server_port    = server_port
                settings.spider_port    = spider_port
                settings.save()
                notices.append('Update Success')
            except Exception,e:
                notices.append(e)
            
    return render_to_response('address.html',
                               {'settings':settings,
                                'notices':notices},
                               context_instance = RequestContext(request))

def server(request):
    projects = json_get_server('listprojects.json')['projects']
    return render_to_response('server.html',
                              {'projects':projects,
                               'settings':settings,
                               },
                              context_instance = RequestContext(request))
def project(request,project_name):
    
    return render_to_response('project.html',
                              {},
                              context_instance = RequestContext(request))

def cache(request):
    data = jsonrpc_call_server('cache', 'keys', pattern='*')
    return HttpResponse(data)

def test(request):
    t = get_template('login_bar_test.html')
    c = Context(locals())
    resp = HttpResponse(t.render(c))
    return resp
