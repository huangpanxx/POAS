# -*- coding: utf-8 -*-

'''
Created on 2012-7-3

@author: snail
'''

from scrapy.contrib.spiders.crawl import Rule, CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from crawler.items import CrawlItem 
from crawler.algorithm.news_extractor import parseHtml

import datetime
import hashlib

from crawler.utils.charset import decodeHtml


class SinaSpider(CrawlSpider):
    
    #settings for model
    site_name = '新浪' 
    name = 'sina' 
    domain = 'news.sina.com.cn' 
    model_type = '新闻' 
    
    #settings for crawlspider
    allowed_domains = [domain] 
    start_urls = ['http://news.sina.com.cn'] 
    
    rules = ( 
             Rule(SgmlLinkExtractor(allow=(r'http://news.sina.com.cn/.*?'),deny=('.*html'))),
             
             Rule(SgmlLinkExtractor(allow=(r'http://news.sina.com.cn/.*?/.*?html'),
                                    deny=(r'http://news.sina.com.cn/photo')),
                  callback='check_response'),
             )
    
    def check_response(self,response):
        return  self.parse_detail(response)
        
    def parse_detail(self,response):

        url = response.url
        item = CrawlItem(url            =   url,
                         site           =   self.site_name,
                         crawl_datetime =   datetime.datetime.now(),
                         uuid           =   hashlib.md5(url).hexdigest(),
                         )
        
        #数据
        data = response.body
     
        #转换到utf8编码
        html = decodeHtml(data)
        
        #解析
        info = parseHtml(html) 
        item['publish_datetime'] = info['datetime']
        item['title'] = info['title']
        item['content'] = info['text']
        
        return item
    