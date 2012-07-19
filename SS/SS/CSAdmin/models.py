from django.db import models

# Create your models here.

class CSAdminSettings(models.Model):
    server_address = models.CharField(max_length=255,default='127.0.0.1')#'10.250.62.12')
    server_port     = models.IntegerField(default=6800)
    spider_port     = models.IntegerField(default=6080)
    
    def __init__(self):
        super(CSAdminSettings,self).__init__()

flag = False

try:
    flag = CSAdminSettings.objects.count() > 0
except:
    flag = False
    
if flag:
    settings = CSAdminSettings.objects.get()[0]
else:
    settings = CSAdminSettings()