#coding:utf8
'''
Created on 2012-7-18

@author: snail
'''

    
from crawl.cache import cache
from scrapyd.webservice import WsResource
from scrapy.conf import settings

class CacheResource(WsResource):
    ws_name = 'cache'
    def render_GET(self,txrequest):
        try:
            op = txrequest.args['op'][0]
            if op == 'clearKey':
                key = txrequest.args['key'][0]
                cache.clearKey(key)
                return True
            if op == 'keys':
                pattern = txrequest.args['key'][0]
                return cache.keys(pattern)
            if op == 'deleteItem':
                key = txrequest.args['key'][0]
                url = txrequest.args['url'][0]
                cache.deleteItem(key, url)
                return True
            if op == 'items':
                key = txrequest.args['key'][0]
                return cache.items(key)
        except KeyError:
            return {'error':'param is missing'}
        except Exception:
            return {'error':'unknown'}
        
class ItemResource(WsResource):
    ws_name = 'item'
    page_dir = settings['PAGE_DIRECTORY']
    def render_GET(self,txrequest):
        try:
            uuid = txrequest.args['uuid'][0]
            path = r'%s/%s' % (self.page_dir,uuid) #攻击危险,检查uuid合法性（数字+字母)
            f = open(path)
            data = f.read()
            return {'content' : data}
        except KeyError:
            return {'error':'param uuid is needed'}
        except IOError:
            return {'error':'file not exist'}
        except Exception,e: #@UnusedVariable
            return {'error':'unknow'}

            