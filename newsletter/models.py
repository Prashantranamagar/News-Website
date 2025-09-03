from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Newsletter(models.Model):
    
    txt = models.CharField(max_length=50)
    status = models.IntegerField()
    
    def __str__(self):
        return self.txt