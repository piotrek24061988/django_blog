from django.db import models
from django.utils import timezone


class Source(models.Model):
    title = models.CharField(max_length=100)
    link = models.TextField()
    country = models.CharField(max_length=50)


class News(models.Model):
    title = models.CharField(max_length=100)
    link = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
