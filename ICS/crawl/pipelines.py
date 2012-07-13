#coding:utf8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topCrawl/item-pipeline.html

from common.model.models import CrawlModel
from scrapy.exceptions import DropItem

class CrawlPipeline(object):
    def __init__(self):
        pass
    
    def dropIfDumplicated(self,item,spider): 
        url = item['url']
        if CrawlModel.objects.filter(url=url).exists():
            raise DropItem()
 
    def process_item(self, item, spider):
        self.dropIfDumplicated(item,spider)
        item.save()
        return item


from datetime import date,datetime
#import json

def _default(obj):
    if isinstance(obj,datetime):
        return unicode(obj.strftime(u'%Y-%m-%dT%H:%M:%S'))
    elif isinstance(obj,date):
        return unicode(obj.strftime(u'%Y-%m-%d'))
    else:
        raise TypeError('%r is not JSON serializable' % obj)
 
class JsonPipeline(object): 
    def process_item(self,item,spider):
        d = dict(item)
        chunks = []
        for key,value in d.items():
            if key != 'content':
                chunks.append('%s:%s' % (key,value))
                
        line =  '\r\n'.join(chunks)
            
        f = open('data/%s' % item['title'],'w')
        
        f.write(line+'\r\n')
        
        f.write(item['content'])
        
        f.close()
        
