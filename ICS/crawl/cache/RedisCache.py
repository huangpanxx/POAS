'''
Created on 2012-7-11

@author: snail
'''
import redis
from common.settings import settings
    
r = redis.Redis(host = settings.REDIS_HOST,port = settings.REDIS_PORT)

def checkDumplicated(dicName,url):
    flag = r.hexists(dicName,url)
    if not flag:
        r.hset(dicName, url,1)
    return flag

def clearCache(dicName):
    r.delete(dicName)
    