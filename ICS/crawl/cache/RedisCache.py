'''
Created on 2012-7-11

@author: snail
'''
import redis
from common.settings import settings
    
r = redis.Redis(host = settings.REDIS_HOST,port = settings.REDIS_PORT)

def checkDumplicated(self,url):
    flag = self.r.hexists(self.name,url)
    if not flag:
        self.r.hset(self.name, url,1)
        return flag
    