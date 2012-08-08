from django.db import models

# Create your models here.
class Lexical(models.Model):
    value = models.CharField(max_length = 255)
    length = models.IntegerField()
    part_of_speech = models.CharField(max_length = 255)
    field = models.CharField(max_length = 255)
    total_weight = models.FloatField()
    date = models.DateField()
    def __str__(self):
        return self.value.encode('utf-8')
    class Meta:
        db_table = 'Lex'

class Doc(models.Model):
    url = models.CharField(max_length = 255)
    path = models.CharField(max_length = 255)
    length = models.IntegerField()
    size = models.IntegerField()
    source_type = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    field = models.CharField(max_length = 255)
    date = models.DateField()
    def __str__(self):
        return self.title.encode('utf-8')
    
    class Meta:
        db_table = 'Document'
    
class Lex_Doc(models.Model):
    Lex = models.ForeignKey(Lexical)
    Doc = models.ForeignKey(Doc)
    times = models.IntegerField()
    first_pos = models.IntegerField()
    weight = models.FloatField()
    date = models.DateField()
    class Meta:
        db_table = 'Lex_Doc'
        
class IDF(models.Model):
    value = models.CharField(max_length = 255)
    field = models.CharField(max_length = 255)
    weight = models.FloatField()
    class Meta:
        db_table = 'IDF'
