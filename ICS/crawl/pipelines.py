#coding:utf8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topCrawl/item-pipeline.html

from common.model.models import CrawlModel
from scrapy.exceptions import DropItem
import json

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

class JsonPipeline(object): 
    def __init__(self):
        self.file = open('items.json','w')
        
    def process_item(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False)
        self.file.write(line.encode('utf8')+'\r\n')
        
