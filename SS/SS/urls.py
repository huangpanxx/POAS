from django.conf.urls.defaults import patterns, include, url
import csadmin
import hot
import personal

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.http import HttpResponseRedirect
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SS.views.home', name='home'),
    # url(r'^SS/', include('SS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    url(r'^admin/super/', include(admin.site.urls)),
    url(r'^admin/$', lambda x: HttpResponseRedirect('./super/')),
    url(r'^admin/cs/', include(csadmin.urls)),
    url(r'^personal/', include(personal.urls)),
    url(r'^hot/',include(hot.urls)),
    url(r'^grappelli/',include('grappelli.urls')),
    
) 
