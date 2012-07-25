# Create your views here.
#coding:utf8
from .models import settings
from django.http import HttpResponse, HttpResponseRedirect
from .utils import jsonrpc_call_server
from django.template.loader import get_template
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
from csadmin.utils import json_get_server, json_post_server

#配置爬虫服务器地址
def address(request):
    notices = []
    if request.method == "POST":
        server_address = request.POST.get('server_address', '')
        server_port = request.POST.get('server_port', '')
        spider_port = request.POST.get('spider_port', '')
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
                settings.server_port = server_port
                settings.spider_port = spider_port
                settings.save()
                notices.append('Update Success')
            except Exception, e:
                notices.append(e)
            
    return render_to_response('address/address.html',
                               {'settings':settings,
                                'notices':notices},
                               context_instance=RequestContext(request))

#服务器相关信息
def server(request):
    projects = json_get_server('listprojects.json')
    return render_to_response('server/server.html',
                              {'projects':projects,
                               'settings':settings,
                               },
                              context_instance=RequestContext(request))
    
def project_version(request, project_name):
    projects = json_get_server('listprojects.json')
    versions = json_get_server('listversions.json', project=project_name)
    return render_to_response('project/project_version.html',
                              {'projects':projects,
                               'project_name':project_name,
                               'versions':versions,
                               },
                              context_instance=RequestContext(request))
    
def project_job(request, project_name):
    projects = json_get_server('listprojects.json')
    jobs = json_post_server('listjobs.json', project=project_name)
    return render_to_response('project/project_job.html',
                              {'projects':projects,
                               'project_name':project_name,
                               'jobs':jobs,
                               },
                              context_instance=RequestContext(request)) 
    
def project_spider(request, project_name):
    projects = json_get_server('listprojects.json')
    spiders = json_get_server('listspiders.json', project=project_name)
    return render_to_response('project/project_spider.html',
                              {'projects':projects,
                               'project_name':project_name,
                               'spiders':spiders,
                               },
                              context_instance=RequestContext(request)) 
#项目信息
def project(request, project_name=""):
    if  project_name:
        return HttpResponseRedirect('./%s/version/' % project_name)
    else:
        projects = json_get_server('listprojects.json')
        return render_to_response('project/project_base.html',
                              {'projects':projects,
                               'project_name':project_name,
                               },
                              context_instance=RequestContext(request))

#缓存信息
def cache(request):
    data = jsonrpc_call_server('cache', 'keys', pattern='*')
    return HttpResponse(data)

def test(request):
    t = get_template('login_bar_test.html')
    c = Context(locals())
    resp = HttpResponse(t.render(c))
    return resp


def home(request):
    return HttpResponseRedirect('./server/')


