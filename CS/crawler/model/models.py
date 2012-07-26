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
    url = models.CharField(max_length=255, blank=True, null=True) #网址
    domain = models.CharField(max_length=255, blank=True, null=True) #域名
    site = models.CharField(max_length=255, blank=True, null=True) #网站名字
    title = models.CharField(max_length=255, blank=True, null=True) #标题
    commentNbr = models.IntegerField(max_length=255, blank=True, null=True) #评论数
    publish_datetime = models.DateTimeField(max_length=255, blank=True, null=True) #发表日期
    crawl_datetime = models.DateTimeField(max_length=255, blank=True, null=True) #爬取日期
    field = models.CharField(max_length=255, blank=True, null=True) #领域
    model_type = models.CharField(max_length=255, blank=True, null=True) #来源类型
    uuid = models.CharField(max_length=255, blank=True, null=True) #内容存放地址
    save_path = models.CharField(max_length=255) #正文存储地址
    

#Spider设置
class Spider(models.Model):
    '''
    Spider 设置
    '''
    spider_name = models.CharField(max_length=255) #Spider名字
    domain = models.CharField(max_length=255) #域名
    
#Spider 起始url集合
class StartUrl(models.Model):
    '''
    Spider 起始Url 
    '''
    spider = models.ForeignKey(Spider)
    url = models.CharField(max_length=255)
    
#item 分类  
class Category(models.Model):
    '''
    Spider url 分类
    '''
    spider = models.ForeignKey(Spider) 
    url_pattern = models.CharField(max_length=255)#url模式
    field = models.CharField(max_length=255) #领域
    site = models.CharField(max_length=255) #网站名字
    model_type = models.CharField(max_length=255) #来源类型
    
#spider 抓取/忽略列表
class UrlPattern(models.Model):
    '''
    Spider url 抓取/忽略 列表
    '''
    spider = models.ForeignKey(Spider)
    pattern = models.CharField(max_length=255)
    is_allow = models.BooleanField(default=True)
    
