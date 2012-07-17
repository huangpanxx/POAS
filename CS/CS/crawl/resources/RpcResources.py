#coding:utf8
'''
Created on 2012-7-17

@author: snail
'''
from scrapy.webservice import JsonResource, JsonRpcResource

class ItemResource(JsonRpcResource):
    ws_name = 'item'
    def __init__(self, crawler, spider_name=None):
        JsonResource.__init__(self, crawler)
        
    def render_GET(self, request):
        return '123'
