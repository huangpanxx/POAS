from django.db import models

# Create your models here.
class Lexical(models.Model):
    value = models.CharField(max_length = 255)
    length = models.IntegerField()
    part_of_speech = models.CharField(max_length = 255)
    field = models.CharField(max_length = 255)
    total_weight = models.FloatField()
    date = models.DateField()
    def __unicode__(self):
        return self.value
    class Meta:
        db_table = 'Lex'

class Doc(models.Model):
    url = models.CharField(max_length = 255)
    path = models.CharField(max_length = 255)
    length = models.IntegerField()
    size = models.IntegerField()
    source_type = models.CharField(max_length = 255)
    field = models.CharField(max_length = 255)
    date = models.DateField()
    
    class Meta:
        db_table = 'Document'
    
class Lex_Doc(models.Model):
    Lex = models.ForeignKey(Lexical)
    Doc = models.ForeignKey(Doc)
    times = models.IntegerField()
    first_pos = models.IntegerField()
    date = models.DateField()
    class Meta:
        db_table = 'Lex_Doc'
