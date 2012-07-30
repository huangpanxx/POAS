#coding:utf8
from django.conf.urls.defaults import patterns, url, include
from . import views
from django.contrib import admin
from django.http import HttpResponseRedirect

project_urls = patterns('',
                url(r'^(\w+)/version/$', views.project_version),
                url(r'^(\w+)/job/$', views.project_job),
                url(r'^(\w+)/spider/$', views.project_spider),
                url(r'^(\w+)/spider/(\d+)/$', views.spider_info),
                url(r'^(\w*)/?$', views.project),
                        )

cache_urls = patterns('',
                      
                url(r'^$', views.project_cache_list),
                url(r'^(\w*)/$', views.project_cache_keys),
                      )

site_urls = patterns('',
                     url(r'^$', views.select_site),
                     url(r'^(\w+)$',views.site_info)
                     ) 


urls = patterns('',
                url(r'^$', lambda x:HttpResponseRedirect('./server/')),
                url(r'^server/$', views.server),
                url(r'^project/', include(project_urls)),
                url(r'^cache/', include(cache_urls)),
                url(r'^site/',include(site_urls)),
                )
