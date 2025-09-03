from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Comment(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cm = models.TextField()
    news_id = models.IntegerField()
    date = models.CharField(max_length=12)
    time = models.CharField(max_length=10)
    status = models.IntegerField(default=0)
   

    def __str__(self):
        return self.name
    
