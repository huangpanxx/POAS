# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topCrawl/items.html

from scrapy.item import Item, Field #@UnusedImport
from scrapy.contrib_exp.djangoitem import DjangoItem
from model.models import CrawlModel



class CrawlItem(DjangoItem):
    '''
    wrapper for scrapy model
    '''
    django_model = CrawlModel
