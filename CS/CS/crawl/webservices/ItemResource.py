#coding:utf8
'''
Created on 2012-7-17

@author: snail
'''
from scrapy.webservice import JsonRpcResource
from scrapy.conf import settings

page_dir = settings['PAGE_DIRECTORY']

class ItemResource(JsonRpcResource):
    ws_name = 'item'
    def render_GET(self,txrequest):
        try:
            uuid = txrequest.args['uuid'][0]
            path = r'%s/%s' % (page_dir,uuid) #攻击危险,检查uuid合法性（数字+字母)
            f = open(path)
            data = f.read()
            return {'content' : data}
        except KeyError:
            return {'error':'param uuid is needed'}
        except IOError:
            return {'error':'file not exist'}
        except Exception,e: #@UnusedVariable
            return {'error':'unknow'}
