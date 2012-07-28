'''
Created on 2012-7-27

@author: snail
'''
from django.contrib import admin
from csmodel.models import * #@UnusedWildImport

class SiteAdmin(admin.ModelAdmin):
    pass
class FieldAdmin(admin.ModelAdmin):
    pass
class SourceTypeAdmin(admin.ModelAdmin):
    pass
class SpiderAdmin(admin.ModelAdmin):
    pass
class StartUrlAdmin(admin.ModelAdmin):
    pass
class CrawlRuleAdmin(admin.ModelAdmin):
    pass
class ClassifyRuleAdmin(admin.ModelAdmin):
    pass
class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Site, SiteAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(SourceType, SourceTypeAdmin)
admin.site.register(Spider, SpiderAdmin)
admin.site.register(StartUrl, StartUrlAdmin)
admin.site.register(CrawlRule, CrawlRuleAdmin)
admin.site.register(ClassifyRule, ClassifyRuleAdmin)
admin.site.register(Item, ItemAdmin)

