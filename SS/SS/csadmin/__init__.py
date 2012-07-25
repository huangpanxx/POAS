#coding:utf8
from django.conf.urls.defaults import patterns, url
from . import views

urls = patterns('',
                url(r'^server/$',views.server),
                url(r'^address/$',views.address),
                url(r'^project/(.*?)/$',views.project),
                url(r'^cache/$',views.cache),
                url(r'^test/$',views.test),
                )