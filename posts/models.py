from django.db import models
from datetime import datetime

# Create your models here.

class posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    tags = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    comments = models.IntegerField()
    author=models.CharField(max_length=1000)