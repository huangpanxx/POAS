#coding:utf8
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from csadmin.utils import json_get_server, json_post_server, jsonrpc_call_server
from django.conf import settings

cs_server = settings.CRAWLSERVER
 

#服务器相关信息
def server(request):
    settings = cs_server
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
    
def spider_settings(request, project_name, spider_name):
    return HttpResponse('Not Implement')


def site(request, project_name):
    sites = jsonrpc_call_server('os', '__str__')
    return HttpResponse(sites)
