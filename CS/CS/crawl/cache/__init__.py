#!/usr/bin/python
#coding:utf8

from scrapy.conf import settings
from scrapy.utils.misc import load_object
import new

class EmptyCache(object):
    def existKey(self,key,url):
        return False

    def clearKey(self,key):
        pass

    def setItem(self,key,url): 
        pass

    def deleteItem(self,key,url):
        pass
    
    def keys(self,pattern):
        return []
    
    def items(self,key):
        return []
    
_cacheTypeStr = settings.get('CACHE')
if _cacheTypeStr:
    _cacheType = load_object(_cacheTypeStr)
    cache = _cacheType()
else:
    cache = EmptyCache()
