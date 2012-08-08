from django.conf.urls import patterns
from wap import views
urls = patterns('',
                '^login/$', views.login_view,
                 )
