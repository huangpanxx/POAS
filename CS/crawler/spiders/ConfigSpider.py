#coding:utf8
'''
Created on 2012-7-26

@author: snail
'''

from crawler.model.models import Spider as SpiderSetting
from scrapy.contrib.spiders.crawl import CrawlSpider, Rule
from crawler.items import CrawlItem
import datetime
import hashlib
from crawler.utils.charset import decodeHtml
from crawler.algorithm.news_extractor import parseHtml
from crawler.utils import create_class
import re
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


#template
class ConfigSpiderBase(CrawlSpider):
    
    #config for spider
    name = '' #名字
    
    #config for crawl 
    allowed_domains = []  #允许的域名
    start_urls = []  #起始地址
    rules = () #爬取规则
    
    #config for classify
    classify_rules = []
    
 
    def get_item(self,response):
        url = response.url
        item = CrawlItem(
                         url            =   url,
                         uuid           =   hashlib.md5(url).hexdigest(),
                         crawl_datetime =   datetime.datetime.now(),
                        )
        return item
    
    def extract_and_fill(self,item,data):
        html = decodeHtml(data) #转换到utf8编码
        info = parseHtml(html) #解析
        
        item['publish_datetime'] = info['datetime']
        item['title'] = info['title']
        item['content'] = info['text']
        
    def parse_detail(self,response):
        url = response.url
        rule = self.classify(url)
        if rule:
            item = self.get_item(response) 
            item['classify_rule'] = rule
            data = response.body #数据
            self.extract_and_fill(item, data)
            return item
        else:
            return None
        
    
    def classify(self,url):
        for rule in self.classify_rules: 
            pattern = rule.url_pattern
            if re.match(pattern, url):
                return rule
        return None
 
def _config_spider(spider_cls,spider_setting):
    #爬虫名字
    spider_cls.name = spider_setting.name
    
    #抓取设置
    site = spider_setting.site
    spider_cls.allowed_domains = [site.domain] #域名
    
    start_urls = [] #起始地址
    for start_url in spider_setting.starturl_set.filter(is_active=True):
        url = start_url.url
        start_urls.append(url)
    spider_cls.start_urls = start_urls
    
    allows_parse = [] #抓取规则 
    denys_parse = [] 
    allows_not_parse = []
    denys_not_parse = []
    for rule in spider_setting.crawlrule_set.filter(is_active=True): 
        pattern = rule.url_pattern
        is_allow = rule.is_allow
        is_parse = rule.is_parse
        if is_parse:
            if is_allow:
                url_list = allows_parse
            else:
                url_list = denys_parse
        else:
            if is_allow:
                url_list = allows_not_parse
            else:
                url_list = denys_not_parse
                
        url_list.append(pattern)
    rule_not_parse = Rule(SgmlLinkExtractor(allow=allows_not_parse,deny=denys_not_parse))
    rule_parse = Rule(SgmlLinkExtractor(allow=allows_parse,deny=denys_parse),callback='parse_detail')
    spider_cls.rules = [rule_not_parse,rule_parse]
    
    #分类设置
    classify_rules = spider_setting.classifyrule_set.filter(is_active=True)
    spider_cls.classify_rules = list(classify_rules)
            
    
def _create_config_spider(cls_name,spider_setting):
    #创建爬虫类 
    cls = create_class(cls_name,(ConfigSpiderBase,))
    #配置爬虫类
    _config_spider(cls,spider_setting)
    
    return cls
    
    
#从数据库生成爬虫类
for i, setting in enumerate(SpiderSetting.objects.all()):
    if setting.is_active:
        cls_name = 'Spider%s' % (i,) 
        cls = _create_config_spider(cls_name, setting)
        #将类放入全局 
        print cls
        globals()[cls_name] = cls 
        del cls

#clean
del ConfigSpiderBase #删除该模板类 