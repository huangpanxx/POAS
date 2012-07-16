#coding:utf8
from scrapy.http import Request
from crawl.cache import cache
from scrapy.exceptions import DropItem

class RedisFilterMiddleware(object):
    def process_spider_input(self,response, spider):
        dicName = spider.name
        url = response.url
        if not (url in spider.start_urls):
            if cache.exist(dicName, url): #@UndefinedVariable
                raise DropItem()
            cache.setCache(dicName, url) #@UndefinedVariable

    def process_spider_output(self,response, result, spider):
        for result in result:
            flag = True
            if isinstance(result,Request):
                flag = not cache.exist(spider.name, result.url) #@UndefinedVariable
            if flag:
                yield result
                
    def process_spider_exception(self,response, exception, spider):
        return [] #ignore item
