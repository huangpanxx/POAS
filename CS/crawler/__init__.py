#coding:utf8
from crawler import settings
#除始化Django存储模型
#os.environ.has_key('DJANGO_SETTINGS_MODULE'):
from django.core.management import setup_environ
setup_environ(settings)
#同步数据库
from django.core.management import execute_manager
execute_manager(settings,[__file__,'syncdb'])
