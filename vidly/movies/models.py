from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movies(models.Model):
    title = models.CharField(max_length=50)
    rent = models.IntegerField()
    stock = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
