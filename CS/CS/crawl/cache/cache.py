'''
Created on 2012-7-16

@author: snail
'''

import redis
from scrapy.conf import settings

    
class RedisCache(object):
    
    r = redis.Redis(host = settings['REDIS_HOST'],port = settings.getint('REDIS_PORT',8086))
    
    def __init__(self):
        pass

    def exist(self,dicName,url):
        return self.r.hexists(dicName,url)

    def clearCache(self,dicName):
        self.r.delete(dicName)

    def setCache(self,dicName,url): 
        self.r.hset(dicName,url,1)

    def deleteCache(self,dicName,url):
        self.r.hdel(dicName,url)
        
        