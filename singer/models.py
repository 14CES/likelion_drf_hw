from django.db import models

# Create your models here.

class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    content = models.TextField()
    debut = models.DateField()

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    release = models.DateField()
    content = models.TextField()