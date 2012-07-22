# Scrapy settings for server project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'server'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['server.spiders']
NEWSPIDER_MODULE = 'server.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

