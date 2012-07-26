#coding:utf8
'''
Created on 2012-7-26

@author: snail
'''

import SinaSpider
from crawler.model.models import Spider as SpiderSetting
from scrapy.contrib.spiders.crawl import CrawlSpider

class ConfigSpiderBase(SinaSpider.SinaSpider):
    pass
        
    
def _create_spider(class_name, bases=(object,), attributes={}):
    cls = type.__new__(type, class_name, bases, attributes)
    super(type, cls).__init__(class_name, bases, attributes)
    return cls

for i, setting in enumerate(SpiderSetting.objects.all()):
    cls_name = 'Spider%s' % (i,)
    cls = _create_spider(cls_name, (CrawlSpider,))
    cls.name = setting.spider_name
    
    #切换名字
    globals()[cls_name] = cls 
    del cls
