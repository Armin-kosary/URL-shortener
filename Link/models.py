from django.db import models

# Create your models here.

class Link(models.Model):
    link_address = models.CharField(max_length=1000)
    short_link = models.CharField(max_length=100)