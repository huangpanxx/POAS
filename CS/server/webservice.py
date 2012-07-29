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
        JsonRpcResource.__init__(self, crawler, os)

from script import config
class ConfigResource(JsonRpcResource):
    ws_name = 'config'
    def __init__(self, crawler):
        JsonRpcResource.__init__(self, crawler, config)


import platform
class PlatformResource(JsonRpcResource):
    ws_name = 'platform'
    def __init__(self,crawler):
        JsonRpcResource.__init__(self,crawler,platform)
        
