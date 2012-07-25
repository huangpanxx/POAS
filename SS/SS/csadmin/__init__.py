#coding:utf8
from django.conf.urls.defaults import patterns, url
from . import views

urls = patterns('',
                url(r'^$',views.home),
                url(r'^server/$',views.server),
                url(r'^address/$',views.address),
                url(r'^project/(\w+)/version/$',views.project_version),
                url(r'^project/(\w+)/job/$',views.project_job),
                url(r'^project/(\w+)/spider/$',views.project_spider),
                url(r'^project/(\w*)/?$',views.project),
                url(r'^cache/$',views.cache),
                url(r'^test/$',views.test),
                )