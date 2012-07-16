#!/usr/bin/python
#coding:utf8

from scrapy.conf import settings
from scrapy.utils.misc import load_object
import new

class EmptyCache(object):
    def exist(self,dicName,url):
        return False

    def clearCache(self,dicName):
        pass

    def setCache(self,dicName,url): 
        pass

    def deleteCache(self,dicName,url):
        pass

_cacheTypeStr = settings['CACHE'] 
_cacheType = load_object(_cacheTypeStr)
cache = _cacheType()
