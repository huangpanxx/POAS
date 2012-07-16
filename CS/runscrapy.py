#coding:utf8
'''
Created on 2012-7-13

@author: snail
'''

from scrapy.cmdline import execute

#除始化Django存储模型
#if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
from django.core.management import setup_environ
from common.settings import settings
setup_environ(settings,'common.settings')

execute()