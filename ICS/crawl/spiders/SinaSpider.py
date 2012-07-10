'''
Created on 2012-7-3

@author: snail
'''

# -*- coding: utf-8 -*-

from scrapy.contrib.spiders.crawl import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector.lxmlsel import HtmlXPathSelector
from crawl.items import CrawlItem

class SinaSpider(CrawlSpider):

    name = 'sina'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com']
    rules = (
             Rule(SgmlLinkExtractor(allow=(r'http://\w+.weibo.com/\w+/\w+')),callback='parse_detail'),
             )
    
    def parse_detail(self,response):
        url = response.url
        hxs = HtmlXPathSelector(response)
        title = hxs.select('//title/text()').extract()[0]
        return CrawlItem(url=url,title=title)
    
