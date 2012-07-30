'''
Created on 2012-7-27

@author: snail
'''
from django.contrib import admin
from csmodel.models import * #@UnusedWildImport

class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'domain')
    list_display_links = list_display
    
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = list_display
    
class SourceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = list_display

class SpiderAdmin(admin.ModelAdmin):
    list_display = ('site', 'name' , 'create_datetime',
                    'last_update', 'update_duration',
                    'is_active')
    list_display_links = list_display
    
class StartUrlAdmin(admin.ModelAdmin):
    list_display = ('spider', 'name', 'url', 'is_active')
    list_display_links = list_display
    
class CrawlRuleAdmin(admin.ModelAdmin):
    list_display = ('spider', 'name', 'url_pattern', 'is_allow',
                    'is_active', 'is_parse')
    list_display_links = list_display

class ClassifyRuleAdmin(admin.ModelAdmin):
    list_display = ('spider', 'source_type', 'field', 'url_pattern', 'is_active')
    
    list_display_links = list_display
    
class ItemAdmin(admin.ModelAdmin):
    list_display = (
                        'title', 'url', 'uuid' ,
                        'save_path', 'comment_number',
                         'publish_datetime',
                          'crawl_datetime' ,
                          'classify_rule',
                    )
    list_display_links = list_display

admin.site.register(Site, SiteAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(SourceType, SourceTypeAdmin)
admin.site.register(Spider, SpiderAdmin)
admin.site.register(StartUrl, StartUrlAdmin)
admin.site.register(CrawlRule, CrawlRuleAdmin)
admin.site.register(ClassifyRule, ClassifyRuleAdmin)
admin.site.register(Item, ItemAdmin)

