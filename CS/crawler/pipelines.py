#coding:utf8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topcrawler/item-pipeline.html

from .model.models import Item
from scrapy.exceptions import DropItem
from scrapy.conf import settings
import os


class ValidationPipeline(object):
    def process_item(self, item, spider):
        if (not item['content']) or (not item['publish_datetime']) or (not item['title']):
            raise DropItem()
        return item
    
class CheckDumplicatedPipeline(object):
    def process_item(self, item, spider): 
        url = item['url'] 
        if Item.objects.filter(url=url).exists():
            raise DropItem()
        else:
            return item

class DbPipeline(object): 
    def process_item(self, item, spider):
        item.save()
        return item
    
class ContentSavePipeline(object): 
    page_dir = settings['PAGE_DIRECTORY']
    def __init__(self):
        self.make_if_missing(self.page_dir)
            
    def make_if_missing(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            
    def save_to(self, path, content):
        open(path, 'w').write(content)
        
    def make_dir(self, item):
        rule = item['classify_rule']
        
        site = rule.spider.site.name.encode('utf8')
        field = rule.field.name.encode('utf8')
        source_type = rule.source_type.name.encode('utf8')
        
        d = item['crawl_datetime']
        crawl_datetime = '%s-%s-%s' % (d.year, d.month, d.day)
        
        
        save_dir = '%s/%s/%s/%s' % (crawl_datetime, site, source_type, field)
        return save_dir
              
    def process_item(self, item, spider): 
        relate_dir = self.make_dir(item)
        save_dir = '%s/%s' % (self.page_dir,relate_dir)
        self.make_if_missing(save_dir)
        
        uuid = item['uuid'] 
        save_path = '%s/%s' % (save_dir, uuid) 
        
        self.save_to(save_path, item['content'])
        item['save_path'] = relate_dir
        return item
         
         
class PlainTextPipeline(object): 
    def process_item(self, item, spider):
        if not item['title']:
            raise DropItem() 
        
        d = dict(item)
        chunks = []
        for key, value in d.items():
            if key != 'content':
                chunks.append('%s:%s' % (key, value))
                
        line = '\r\n'.join(chunks)
            
        uuid = item['uuid']
        
        f = open(r'%s/%s' % (self.page_dir, uuid), 'w')
        f.write(line + '\r\n')
        f.write(item['content'])
        f.close()
        
