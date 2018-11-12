from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(blank=False, null=False)
    content = models.TextField(blank=False, null=False, default='No Data')
    timestamp = models.DateTimeField(auto_now_add=True)
    
