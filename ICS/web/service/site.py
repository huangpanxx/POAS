'''
Created on 2012-7-9

@author: snail
'''
from django.conf.urls.defaults import patterns, url
from web.service import views

urls = patterns('',
    url(r'^$',views.home),
)
