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
    url            = models.CharField(max_length=255,blank=True,null=True)
    domain         = models.CharField(max_length=255,blank=True,null=True)
    title          = models.CharField(max_length=255,blank=True,null=True)
    UDDI           = models.CharField(max_length=255,blank=True,null=True)
    commentNumber  = models.IntegerField(max_length=255,blank=True,null=True)
    datetime       = models.DateTimeField(max_length=255,blank=True,null=True)
    
    class Meta:  
        verbose_name = "舆论数据"  
        verbose_name_plural = "舆论数据"
        
    def __unicode__(self):
        return self.title + u'\t\t' + unicode(self.datetime)