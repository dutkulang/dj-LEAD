from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=350)
    data = models.TextField()