from django.db import models

# Create your models here.

class CSAdminSettings(models.Model):
    server_address = models.CharField(max_length=255, default='192.168.0.1')#'10.250.62.12')
    server_port = models.IntegerField(default=6800)
    spider_port = models.IntegerField(default=6080)
    
    def __init__(self):
        super(CSAdminSettings, self).__init__()
        

is_exist = False

try:
    is_exist = len(CSAdminSettings.objects.filter('...')) > 0
except:
    is_exist = False
    
if is_exist:
    settings = CSAdminSettings.objects.all()[0]
else:
    settings = CSAdminSettings()
