from pydoc import describe
from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()