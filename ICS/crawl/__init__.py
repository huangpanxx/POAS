#coding:utf8
import os
#始化Django存储模型
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
    from django.core.management import setup_environ
    from model import django_settings
    setup_environ(django_settings)
