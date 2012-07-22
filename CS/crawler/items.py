#coding:utf8
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topcrawler/items.html

from scrapy.item import Field , Item #@UnusedImport
from scrapy.contrib_exp.djangoitem import DjangoItem
from .model.models import CrawlModel


#class CrawlItem(Item):
#    url                 = Field() #网址
#    domain              = Field() #域名
#    site                = Field() #网站名字
#    title               = Field() #标题
#    commentNbr          = Field() #评论数
#    publish_datetime    = Field() #发表日期
#    crawl_datetime      = Field() #爬取日期
#    field               = Field()  #领域
#    model_type          = Field() #类型
#    uuid                = Field() #内容存放地址
#    content             = Field()

class CrawlItem(DjangoItem):
    '''
    wrapper for scrapy model
    '''
    django_model = CrawlModel
    content      = Field()
