#coding:utf8
from crawler import settings
#除始化Django存储模型
#os.environ.has_key('DJANGO_SETTINGS_MODULE'):
from django.core.management import setup_environ
import StringIO
setup_environ(settings)
#同步数据库
import sys
stdout = sys.stdout
sys.stdout = StringIO.StringIO() #静默同步
from django.core.management import execute_manager
execute_manager(settings,[__file__,'syncdb'])
sys.stdout = stdout