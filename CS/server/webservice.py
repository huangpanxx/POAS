#coding:utf8
'''
Created on 2012-7-18

@author: snail
'''

from crawler.cache import cache #@UnresolvedImport
from scrapy.conf import settings
from scrapy.webservice import JsonRpcResource

class CacheResource(JsonRpcResource):
    ws_name = 'cache'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, crawler, cache)
        
class _PageLoader(object):
    page_dir = settings['PAGE_DIRECTORY']
    def getPage(self, name, uuid):
            path = r'%s/%s/%s' % (self.page_dir, name, uuid) #攻击危险,检查uuid合法性（数字+字母)
            return open(path).read()
        
    
class PageResource(JsonRpcResource):
    _page_loader = _PageLoader()
    ws_name = 'page'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, crawler, self._page_loader)
        
import sys
class SystemResource(JsonRpcResource):
    ws_name = 'system'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, crawler, sys)

import os 
class OSResource(JsonRpcResource):
    ws_name = 'os'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, os)
        
from script import config
class ConfigResource(JsonRpcResource):
    ws_name = 'config'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, config)
        
from crawler.model.models import ClassifyRule
class ClassifyRuleResource(JsonRpcResource):
    ws_name = 'classify_rule'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, ClassifyRule.objects)
   
from crawler.model.models import CrawlRule
class CrawlRuleResource(JsonRpcResource):
    ws_name = 'crawl_rule'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, CrawlRule.objects)
   
from crawler.model.models import Field
class FieldResource(JsonRpcResource):
    ws_name = 'field'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, Field.objects)
   
from crawler.model.models import Item
class ItemResource(JsonRpcResource):
    ws_name = 'item'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, Item.objects)
   
from crawler.model.models import Site
class SiteResource(JsonRpcResource):
    ws_name = 'site'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, Site.objects)
   
from crawler.model.models import SourceType
class SourceTypeResource(JsonRpcResource):
    ws_name = 'source_type'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, SourceType.objects)
   
from crawler.model.models import Spider
class SpiderResource(JsonRpcResource):
    ws_name = 'spider' 
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, Spider.objects)
   
from crawler.model.models import StartUrl
class StartUrlResource(JsonRpcResource):
    ws_name = 'start_url'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, StartUrl.objects)
   
