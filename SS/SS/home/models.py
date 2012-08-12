# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Alibaba(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'alibaba'

class Amazon(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'amazon'

class Classifyrule(models.Model):
    id = models.IntegerField(primary_key=True)
    spider_id = models.IntegerField()
    url_pattern = models.CharField(max_length=765)
    field_id = models.IntegerField()
    source_type_id = models.IntegerField()
    is_active = models.IntegerField()
    class Meta:
        db_table = u'classifyrule'

class Crawlrule(models.Model):
    id = models.IntegerField(primary_key=True)
    spider_id = models.IntegerField()
    url_pattern = models.CharField(max_length=765)
    is_allow = models.IntegerField()
    is_active = models.IntegerField()
    name = models.CharField(max_length=765)
    class Meta:
        db_table = u'crawlrule'

class Field(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    class Meta:
        db_table = u'field'

class Gome(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'gome'

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=765)
    uuid = models.CharField(max_length=765)
    title = models.CharField(max_length=765, blank=True)
    save_path = models.CharField(max_length=765)
    comment_number = models.IntegerField(null=True, blank=True)
    publish_datetime = models.DateTimeField(null=True, blank=True)
    crawl_datetime = models.DateTimeField()
    classify_rule_id = models.IntegerField()
    class Meta:
        db_table = u'item'

class Site(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=765)
    name = models.CharField(max_length=765)
    domain = models.CharField(max_length=765)
    class Meta:
        db_table = u'site'

class Sourcetype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    class Meta:
        db_table = u'sourcetype'

class Spider(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    site_id = models.IntegerField()
    create_datetime = models.DateTimeField()
    last_update = models.DateTimeField()
    update_duration = models.IntegerField()
    is_active = models.IntegerField()
    class Meta:
        db_table = u'spider'

class Starturl(models.Model):
    id = models.IntegerField(primary_key=True)
    spider_id = models.IntegerField()
    url = models.CharField(max_length=765)
    name = models.CharField(max_length=765)
    is_active = models.IntegerField()
    class Meta:
        db_table = u'starturl'

class Sunning(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sunning'

class Tecent(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tecent'

class Tendency(models.Model):
    id = models.IntegerField(primary_key=True)
    tendency_value = models.FloatField(null=True, blank=True)
    item_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tendency'

class Valid(models.Model):
    id = models.IntegerField(primary_key=True)
    isvalid = models.CharField(max_length=9, blank=True)
    item_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'valid'

class Vancl(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'vancl'

