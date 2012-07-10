# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topCrawl/item-pipeline.html
import json #@UnusedImport

class CrawlPipeline(object):
    def __init__(self):
        #self.file = open('items.json', 'a')
        pass
        
    def process_item(self, item, spider):
        #line = json.dumps(dict(item),ensure_ascii=False).encode('utf8') + '\n'
        #self.file.write(line)
#        for key in item.keys():
#            value = item[key]
#            if isinstance(value,unicode):
#                item[key] = value.encode('utf8')
        item.save()
        return item
    
