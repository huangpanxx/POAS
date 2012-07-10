# Scrapy settings for crawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topcrawl/settings.html
#

BOT_NAME = 'crawl'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['crawl.spiders']
NEWSPIDER_MODULE = 'crawl.spiders'
DEFAULT_ITEM_CLASS = 'crawl.items.CrawlItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['crawl.pipelines.CrawlPipeline']
