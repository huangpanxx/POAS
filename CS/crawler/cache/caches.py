'''
Created on 2012-7-16

@author: snail
'''

import redis
from scrapy.conf import settings

    
class RedisCache(object):
    
    r = redis.Redis(host = settings['REDIS_HOST'],port = settings.getint('REDIS_PORT',8086))
    
    def existKey(self,key,url):
        return self.r.hexists(key,url)

    def clearKey(self,key):
        self.r.delete(key)

    def setItem(self,key,url): 
        self.r.hset(key,url,1)

    def deleteItem(self,key,url):
        self.r.hdel(key,url)
        
    def keys(self,pattern):
        return self.r.keys(pattern)
    
    def items(self,key):
        return self.r.hkeys(key)
    