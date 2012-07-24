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
    
