from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    Artist = models.CharField(max_length=100)
    Genre= models.CharField(max_length=100)
    Duration= models.CharField(max_length=100)
    
class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    creation_date = models.CharField(max_length=100)
    

    
    

