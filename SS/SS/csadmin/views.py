#coding:utf8
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from csadmin.utils import json_get_server, json_post_server, jsonrpc_call_server
from django.conf import settings
from csmodel.models import Spider, Site

cs_server = settings.CRAWLSERVER
 

#服务器相关信息
def server(request):
    settings = cs_server
    projects = json_get_server('listprojects.json')
    version = jsonrpc_call_server('platform', 'version')
    system = jsonrpc_call_server('platform', 'system')
    architecture = jsonrpc_call_server('platform', 'architecture')
    node = jsonrpc_call_server('platform', 'node')
    platform = jsonrpc_call_server('platform', 'platform')
    machine = jsonrpc_call_server('platform', 'machine')
    processor = jsonrpc_call_server('platform', 'processor')
    python_build = jsonrpc_call_server('platform', 'python_build')
    python_compiler = jsonrpc_call_server('platform', 'python_compiler')
    python_version = jsonrpc_call_server('platform', 'python_version')
    release = jsonrpc_call_server('platform', 'release')
    uname = jsonrpc_call_server('platform', 'uname')
    
#    environ = json_get_server('os/environ')
    
    return render_to_response('server/server.html',
                              {'projects':projects,
                               'settings':settings,
                               'server':{
                                         'version':version,
                                         'system':system,
                                         'architecture':architecture,
                                         'node':node,
                                         'platform':platform,
                                         'machine':machine,
                                         'processor':processor,
                                         'python_build':python_build,
                                         'python_compiler':python_compiler,
                                         'python_version':python_version,
                                         'release':release,
                                         'uname':uname,
                                                    },
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
    
    jobs = json_get_server('listjobs.json', project=project_name)
    
    return render_to_response('project/project_job.html',
                              {'projects':projects,
                               'project_name':project_name,
                               'jobs':jobs,
                               },
                              context_instance=RequestContext(request)) 

def project_spider(request, project_name):
    projects = json_get_server('listprojects.json')
    spiders = Spider.objects.all()
    return render_to_response('project/project_spider.html',
                              {'projects':projects,
                               'project_name':project_name,
                               'spiders':spiders,
                               },
                              context_instance=RequestContext(request)) 
#项目信息 
def project(request, project_name=""):
    if  project_name:
        return HttpResponseRedirect('./%s/spider/' % project_name)
    else:
        projects = json_get_server('listprojects.json')
        return render_to_response('project/select_project.html',
                              {'projects':projects,
                               'project_name':project_name,
                               },
                              context_instance=RequestContext(request))
    
def spider_info(request, project_name, spider_id):
    spiders = Spider.objects.filter(id=int(spider_id))
    
    spider = None
    if spiders.count() > 0:
        spider = spiders[0]
    
    return render_to_response('project/spider/spider.html',
                              {'spider':spider,
                               'spiders':spiders,
                               'project_name':project_name,
           },
        context_instance=RequestContext(request))
    
def project_cache_list(request):
    keys = jsonrpc_call_server('cache', 'keys', pattern='*')
    return render_to_response('cache/select_cache.html',
                              {
                               'keys':keys,
           },
        context_instance=RequestContext(request))

def project_cache_keys(request, cache_key):
    items = jsonrpc_call_server('cache', 'items', cache_key)
    keys = jsonrpc_call_server('cache', 'keys', pattern='*')
    return render_to_response('cache/cache_info.html',
                              {
                               'keys':keys,
                               'items':items,
                               'cache_name':cache_key,
           },
        context_instance=RequestContext(request))
    
def select_site(request):
    sites = Site.objects.all()
    return render_to_response('site/select_site.html',
                              {
                               'sites':sites,
           },
        context_instance=RequestContext(request))
   
   
def site_info(request, site_id):
    _sites = Site.objects.filter(id=int(site_id))
    sites = Site.objects.all()
    site = None
    if _sites.count():
        site = _sites[0]
    
    return render_to_response('site/site_info.html',
                              {
                               'sites':sites,
                               'site':site
           },
        context_instance=RequestContext(request))
   

