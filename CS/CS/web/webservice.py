#coding:utf8
'''
Created on 2012-7-18

@author: snail
'''

    
from crawl.cache import cache
from scrapy.conf import settings
from scrapy.webservice import JsonRpcResource

class CacheResource(JsonRpcResource):
    ws_name = 'cache'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, crawler, cache)
        
class _PageLoader(object):
    page_dir = settings['PAGE_DIRECTORY']
    def getPage(self,uuid):
            path = r'%s/%s' % (self.page_dir, uuid) #攻击危险,检查uuid合法性（数字+字母)
            return open(path).read()
        
_page_loader = _PageLoader()
    
class ItemResource(JsonRpcResource):
    ws_name = 'item'
    def __init__(self,crawler):
        JsonRpcResource.__init__(self, crawler,_page_loader)

