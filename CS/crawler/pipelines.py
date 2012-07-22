#coding:utf8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topcrawler/item-pipeline.html

from .model.models import CrawlModel
from scrapy.exceptions import DropItem
from scrapy.conf import settings
import os

page_dir = settings['PAGE_DIRECTORY']

class ValidationPipeline(object):
    def process_item(self,item,spider):
        if (not item['content']) or (not item['publish_datetime']) or (not item['title']):
            raise DropItem()
        return item
    
class CheckDumplicatedPipeline(object):
    def process_item(self,item,spider): 
        url = item['url']
        if CrawlModel.objects.filter(url=url).exists():
            raise DropItem()
        else:
            return item

class DbPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item
    
class ContentSavePipeline(object): 
    def __init__(self):
        if not os.path.exists(page_dir):
            os.mkdir(page_dir)
            
    def process_item(self,item,spider): 
        uuid = item['uuid']
        f = open(r'%s/%s' % (page_dir,uuid),'w')
        f.write(item['content'])
        f.close()
   
         
         
#def _default(obj):
#    if isinstance(obj,datetime):
#        return unicode(obj.strftime(u'%Y-%m-%dT%H:%M:%S'))
#    elif isinstance(obj,date):
#        return unicode(obj.strftime(u'%Y-%m-%d'))
#    else:
#        raise TypeError('%r is not JSON serializable' % obj)

class PlainTextPipeline(object): 
    def process_item(self,item,spider):
        if not item['title']:
            raise DropItem()
        
        d = dict(item)
        chunks = []
        for key,value in d.items():
            if key != 'content':
                chunks.append('%s:%s' % (key,value))
                
        line =  '\r\n'.join(chunks)
            
        uuid = item['uuid']
        
        f = open(r'%s/%s' % (page_dir,uuid),'w')
        f.write(line+'\r\n')
        f.write(item['content'])
        f.close()
        
        
