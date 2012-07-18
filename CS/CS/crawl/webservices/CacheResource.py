'''
Created on 2012-7-18

@author: snail
'''
from scrapy.webservice import JsonRpcResource
from crawl.cache import cache #@UnusedImport

class CacheResource(JsonRpcResource):
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
                
            