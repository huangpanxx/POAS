from django.conf.urls.defaults import patterns
from wap import views
urls = patterns('',
                (r'^login/$', views.login_view),
                 )
