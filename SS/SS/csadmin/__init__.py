#coding:utf8
from django.conf.urls.defaults import patterns, url, include
from . import views
from django.contrib import admin

project_urls = patterns('',
                url(r'^(\w+)/version/$', views.project_version),
                url(r'^(\w+)/job/$', views.project_job),
                url(r'^(\w+)/spider/$', views.project_spider),
                url(r'^(\w+)/spider/(\w+)/$', views.project_spider),
                url(r'^(\w+)/site/$', views.site),
                url(r'^(\w*)/site/(\w+)/$', views.site),
                url(r'^(\w*)/?$', views.project),
                        )


urls = patterns('',
                url(r'^$', views.home),
                url(r'^server/$', views.server),
                url(r'^project/', include(project_urls)),
                
                )



