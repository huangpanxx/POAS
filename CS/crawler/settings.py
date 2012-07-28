#coding:utf8
# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topcrawler/settings.html
#

import os

#db settings
PROJECT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../.scrapy')

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': os.path.join(PROJECT_PATH, 'database.db'), # Or path to database file if using sqlite3.
#        'USER': '', # Not used with sqlite3.
#        'PASSWORD': '', # Not used with sqlite3.
#        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '', # Set to empty string for default. Not used with sqlite3.
#    },
             
    'default':{
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'csmodel', # Or path to database file if using sqlite3.
        'USER': 'snail', # Not used with sqlite3.
        'PASSWORD': 'departure', # Not used with sqlite3.
        'HOST': '192.168.0.1', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306', # Set to empty string for default. Not used with sqlite3.
    },
}

#db_path = DATABASES['default']['NAME']
#db_dir = os.path.dirname(db_path)
#
#if not os.path.exists(db_dir):
#    os.mkdir(db_dir)

INSTALLED_APPS = (
     'crawler.model',
)

#scrapy settings

BOT_NAME = 'crawler'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
DEFAULT_ITEM_CLASS = 'crawler.items.CrawlItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
                  'crawler.pipelines.ValidationPipeline',
                  'crawler.pipelines.CheckDumplicatedPipeline',
                  'crawler.pipelines.ContentSavePipeline',
                  'crawler.pipelines.DbPipeline',
                  #'crawler.pipelines.PlainTextPipeline',
                  ]


SPIDER_MIDDLEWARES = {
        'crawler.spidermiddlewares.redisfiltermiddleware.RedisFilterMiddleware': 543, #过滤重复请求
        }

DEPTH_PRIORITY = 1
DEPTH_LIMIT = 2
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

CACHE = 'crawler.cache.caches.RedisCache' 

PAGE_DIRECTORY = os.path.join(PROJECT_PATH, 'pages')


#redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

