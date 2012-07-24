from django.conf.urls.defaults import patterns, include, url
import csadmin
import topic
import personal

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SS.views.home', name='home'),
    # url(r'^SS/', include('SS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    url(r'^admin/super/', include(admin.site.urls)),
    url(r'^admin/$',include(admin.site.urls)),
    url(r'^admin/cs/',include(csadmin.urls)),
    url(r'^topic/',include(topic.urls)),
    url(r'^personal/',include(personal.urls))
    
)
