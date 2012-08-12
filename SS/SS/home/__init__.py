from django.conf.urls.defaults import patterns, url
from home import views
from django.http import HttpResponseRedirect

urls = patterns('',
                url(r'^$',lambda x:HttpResponseRedirect('/classify/')),
                url(r'^classify/',views.classify)
                
                )