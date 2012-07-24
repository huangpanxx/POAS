from django.db import models

# Create your models here.

class Lexical(models.Model):
    value = models.CharField(max_length = 50)
    length = models.IntegerField()
    part_of_speech = models.CharField(max_length = 10)
    total_weight = models.FloatField()
    date = models.DateField()

class Doc(models.Model):
    id = models.IntegerField(primary_key = True)
    url = models.CharField(max_length = 200)
    length = models.IntegerField()
    size = models.IntegerField()
    field = models.CharField(max_length = 10)
    date = models.DateField()
    
class Lex_Doc(models.Model):
    Lexical = models.ForeignKey(Lexical)
    Doc = models.ForeignKey(Doc)
    times = models.IntegerField()
    first_pos = models.IntegerField()
    date = models.DateField()
    
