# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topCrawl/items.html

from scrapy.item import Field 
from scrapy.contrib_exp.djangoitem import DjangoItem
from crawl.model.models import CrawlModel



class CrawlItem(DjangoItem):
    '''
    wrapper for scrapy model
    '''
    django_model = CrawlModel
    content      = Field()
