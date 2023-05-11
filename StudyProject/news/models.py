from django.db import models


# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()


class Comment(models.Model):
    text = models.CharField(max_length=255, verbose_name='Чат')

