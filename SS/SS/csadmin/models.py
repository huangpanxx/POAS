#coding:utf8
'''
Created on 2012-7-9

@author: snail
'''

from django.db import models

###身份描述结构

class Site(models.Model):
    url = models.CharField(max_length=255) #网址
    name = models.CharField(max_length=255) #网站名字
    domain = models.CharField(max_length=255) #域名
    
class Field(models.Model):
    name = models.CharField(max_length=255)  #领域

class SourceType(models.Model): #来源类型
    name = models.CharField(max_length=255)
    
### 爬虫描述
class Spider(models.Model):
    '''
    Spider 设置
    '''
    name = models.CharField(max_length=255) #Spider名字
    site = models.ForeignKey(Site) #负责网站
    
    create_datetime = models.DateTimeField(max_length=255) #创建时间
    update_duration = models.IntegerField(0) #更新间隔(分钟)
    is_active = models.BooleanField(default=False) #是否激活
    
 

#爬虫起始url集合
class StartUrl(models.Model):
    '''
    Spider 起始Url 
    '''
    spider = models.ForeignKey(Spider) #适用爬虫
    url = models.CharField(max_length=255) #地址
    name = models.CharField(max_length=255) #名字
    is_active = models.BooleanField(default=False)  #是否激活
   
#抓取/忽略列表
class CrawlRule(models.Model):
    '''
    Spider 抓取/忽略 列表
    '''
    spider = models.ForeignKey(Spider)              #适用的爬虫 
    url_pattern = models.CharField(max_length=255)  #url模式 
    is_allow = models.BooleanField(default=True)    #抓取/忽略 
    is_active = models.BooleanField(default=False)  #是否激活
    is_parse = models.BooleanField(default=True) #是否解析
 
    
#分类规则 
class ClassifyRule(models.Model):
    '''
    Spider url 分类
    '''
    spider = models.ForeignKey(Spider)              #适用的爬虫
    url_pattern = models.CharField(max_length=255)  #url模式
    field = models.ForeignKey(Field)                #相应领域
    source_type = models.ForeignKey(SourceType)     #来源类型
    is_active = models.BooleanField(default=False)  #是否激活

##数据项描述
class Item(models.Model):
    '''
    django model
    '''
 
    url = models.CharField(max_length=255) #网址
    uuid = models.CharField(max_length=255) #标识
    
    title = models.CharField(max_length=255, blank=True, null=True) #标题
    save_path = models.CharField(max_length=255) #正文存储地址
    comment_number = models.IntegerField(max_length=255, blank=True, null=True) #评论数
    publish_datetime = models.DateTimeField(max_length=255, blank=True, null=True) #发表日期
    crawl_datetime = models.DateTimeField(max_length=255) #爬取日期
    
    classify_rule = models.ForeignKey(ClassifyRule) #匹配规则（能找到爬虫，从而获取来源等)




