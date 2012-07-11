# -*- coding: utf-8 -*-

'''
Created on 2012-7-3

@author: snail
'''

from scrapy.contrib.spiders.crawl import Rule, CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
#from scrapy.selector.lxmlsel import HtmlXPathSelector
from crawl.items import CrawlItem
import datetime
import hashlib

#from crawl.algorithm.extract import parseHtml

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
             Rule(SgmlLinkExtractor(deny=('.*html'))),
             Rule(SgmlLinkExtractor(allow=(r'http://news.sina.com.cn/.*?/.*?html'),
                                    deny=(r'http://news.sina.com.cn/photo')),
                  callback='check_response'),
             )
    
    def check_response(self,response):
                    #检查重复
#        if self.checkDumplicated(url):
#            return
        self.parse_detail(self,response)
        
    def parse_detail(self,response):
#    url                 = models.CharField(max_length=255,blank=True,null=True) #网址
#    domain              = models.CharField(max_length=255,blank=True,null=True) #域名
#    site                = models.CharField(max_length=255,blank=True,null=True) #网站名字
#   *title               = models.CharField(max_length=255,blank=True,null=True) #标题
#   *commentNbr          = models.IntegerField(max_length=255,blank=True,null=True) #评论数
#   *publish_datetime    = models.DateTimeField(max_length=255,blank=True,null=True) #发表日期
#    crawl_datetime      = models.DateTimeField(max_length=255,blank=True,null=True) #爬取日期
#   *field               = models.CharField(max_length=255,blank=True,null=True)  #领域
#    model_type          = models.CharField(max_length=255,blank=True,null=True) #类型
#    uiid                = models.CharField(max_length=255,blank=True,null=True) #内容存放地址

        url = response.url
        item = CrawlItem(url            =   url,
                         domain         =   self.domain,
                         site           =   self.site_name,
                         crawl_datetime =   datetime.datetime.now(),
                         uuid           =   hashlib.md5(url).hexdigest(),
                         model_type     =   self.model_type,
                         )
        
                    #从unicode转换为 utf8
#        html = response
        
#        info = parseHtml(html)
        
#        hxs = HtmlXPathSelector(response)
#        
#        title = ''
#        commentNbr = ''
#        publish_datetime = ''
#        field = ''

        return item
        