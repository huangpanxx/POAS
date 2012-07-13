# -*- coding: utf-8 -*-

'''
Created on 2012-7-3

@author: snail
'''

from scrapy.contrib.spiders.crawl import Rule, CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from crawl.items import CrawlItem
#from scrapy.selector.lxmlsel import HtmlXPathSelector
#from scrapy.http.request import Request
from crawl.algorithm.news_extractor import parseHtml

#import re
import datetime
import hashlib

from crawl.utils.charset import decodeHtml

#    需要解析的字段        
#    url                 = models.CharField(max_length=255,blank=True,null=True) #网址
#    domain              = models.CharField(max_length=255,blank=True,null=True) #域名
#    site                = models.CharField(max_length=255,blank=True,null=True) #网站名字
#   *title               = models.CharField(max_length=255,blank=True,null=True) #标题
#   *commentNbr          = models.IntegerField(max_length=255,blank=True,null=True) #评论数
#   *publish_datetime    = models.DateTimeField(max_length=255,blank=True,null=True) #发表日期
#    crawl_datetime      = models.DateTimeField(max_length=255,blank=True,null=True) #爬取日期
#   *field               = models.CharField(max_length=255,blank=True,null=True)  #领域
#    model_type          = models.CharField(max_length=255,blank=True,null=True) #类型
#    uuid                = models.CharField(max_length=255,blank=True,null=True) #内容存放地址

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
                         domain         =   self.domain,
                         site           =   self.site_name,
                         crawl_datetime =   datetime.datetime.now(),
                         uuid           =   hashlib.md5(url).hexdigest(),
                         model_type     =   self.model_type,
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
    
        #ajax 获取评论数
#        hxs = HtmlXPathSelector(response)
#        
#        _publishid = hxs.select("//meta[@name='publishid']/@content").extract()
#  
#        if _publishid:
#            publishid = _publishid[0].encode('utf-8').replace(',','-')
#            
#            url = 'http://comment5.news.sina.com.cn/page/info?format=js&jsvar=pagedata&channel=cj&newsid=' \
#                    + publishid \
#                    + '&group=0&page=1&list=all&fr=ct'
#                    
#            request =  Request(url, callback=self.parse_ajax)
#            request.meta['item'] = item
#            return request
#        else:
#            return item
#        
#    def parse_ajax(self,response):
#        item = response['item']
#        data = response.body
#        m = re.search('"total": (\d+),',data)
#        if m:
#            cmtNbr = m.group(1)
#            item['commentNbr'] = cmtNbr
#        return item