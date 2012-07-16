#coding:utf8
'''
Created on 2012-7-9

@author: snail
'''

from django.db import models

class CrawlModel(models.Model):
    '''
    django model
    '''
    url                 = models.CharField(max_length=255,blank=True,null=True) #网址
    domain              = models.CharField(max_length=255,blank=True,null=True) #域名
    site                = models.CharField(max_length=255,blank=True,null=True) #网站名字
    title               = models.CharField(max_length=255,blank=True,null=True) #标题
    commentNbr          = models.IntegerField(max_length=255,blank=True,null=True) #评论数
    publish_datetime    = models.DateTimeField(max_length=255,blank=True,null=True) #发表日期
    crawl_datetime      = models.DateTimeField(max_length=255,blank=True,null=True) #爬取日期
    field               = models.CharField(max_length=255,blank=True,null=True)  #领域
    model_type          = models.CharField(max_length=255,blank=True,null=True) #类型
    uuid                = models.CharField(max_length=255,blank=True,null=True) #内容存放地址
    
    class Meta:
        verbose_name = "舆论数据"  
        verbose_name_plural = "舆论数据"
        
    def __unicode__(self):
        return '%(title)s\t\t%(site)s%(publish_datetime)s' % {
            'title':self.title,
            'site':self.site,
            'publish_datetime':unicode(self.publish_datetime)
                        }
    