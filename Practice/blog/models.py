from django.db import models


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=255)
