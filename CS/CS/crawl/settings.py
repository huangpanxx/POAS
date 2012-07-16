#coding:utf8
# Scrapy settings for crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topcrawl/settings.html
#

import os

#db settings
PROJECT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_PATH, 'database.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS = (
     'crawl.model',
)

#scrapy settings

BOT_NAME = 'crawl'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['crawl.spiders']
NEWSPIDER_MODULE = 'crawl.spiders'
DEFAULT_ITEM_CLASS = 'crawl.items.CrawlItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
                  'crawl.pipelines.CheckDumplicatedPipeline',
                  'crawl.pipelines.DbPipeline',
                  'crawl.pipelines.ContentSavePipeline',
#                  'crawl.pipelines.PlainTextPipeline',
                  ]


SPIDER_MIDDLEWARES = {
        'crawl.spidermiddlewares.redisfiltermiddleware.RedisFilterMiddleware': 543, #过滤重复请求
        }

DEPTH_PRIORITY = 1
DEPTH_LIMIT  = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

CACHE = 'crawl.cache.cache.RedisCache' 

PAGE_DIRECTORY = os.path.join(PROJECT_PATH, 'pages')

#redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
