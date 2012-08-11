#coding:utf8
from django.conf.urls.defaults import patterns
from wap import views
urls = patterns('',
                (r'^login/$', views.login_view), #登录
                (r'^help/$', views.help_view), #帮助
                (r'^transport/$',views.transport_view), #传播分析
                (r'^hot/$',views.hot_view), #热点分析
                (r'^topic/$',views.topic_view), #专题检测
                (r'^source/$',views.source_view), #来源分析
                (r'^inbox/$',views.inbox_view),#站内信
                (r'^read_all/$',views.read_all_view),
                (r'^$',views.home_view) #主页
                 )
