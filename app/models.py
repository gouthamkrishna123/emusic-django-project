from django.db import models

# Create your models here.

class customer(models.Model):
    username=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=20)
    conformpassword=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.CharField(max_length=200)


class music(models.Model):
    Typeof=models.CharField(max_length=200, default='SOME STRING')
    title=models.CharField(max_length=200)
    artist=models.CharField(max_length=200)
    image=models.ImageField(upload_to="static/images")
    audio_file=models.FileField(blank=True,upload_to="static/files",null=True)
    audio_link=models.CharField(max_length=500)

class Album(models.Model):
    album_name=models.CharField(max_length=20)
    album_image=models.FileField(upload_to="static/images")

def str_(self):
    return self.album_name

class Songs(models.Model):
    name=models.CharField(max_length=20, default="name")
    album_name=models.ForeignKey(Album,on_delete=models.CASCADE)
    song=models.FileField(upload_to="static/files")
    picture=models.FileField(upload_to="static/images")
    singer=models.CharField(max_length=20)
