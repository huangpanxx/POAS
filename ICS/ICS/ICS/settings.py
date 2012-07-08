# Scrapy settings for ICS project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'ICS'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['ICS.spiders']
NEWSPIDER_MODULE = 'ICS.spiders'
DEFAULT_ITEM_CLASS = 'ICS.items.IcsItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

