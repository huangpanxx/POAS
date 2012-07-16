#!/usr/bin/env python
#coding:utf8
from django.core.management import execute_manager
try:
    import settings
except ImportError:
    import sys
    error = '''加载Django配置文件失败'''
    sys.stderr.write(error)
    sys.exit(1)


if __name__ == "__main__":
    execute_manager(settings)
