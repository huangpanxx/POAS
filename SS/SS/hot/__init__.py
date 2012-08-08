#coding:utf8
from django.conf.urls.defaults import patterns, url
from . import views

urls = patterns('',
                url(r'^$',views.hot),
                url(r'^hot/(?P<word_id>\d+)/$',views.hot_detail),
                )