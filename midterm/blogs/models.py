from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)