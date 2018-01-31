from django.db import models

# Create your models here.
class Classification(models.Model):
    cname=models.CharField(max_length=18)
