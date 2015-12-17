from django.db import models
from django.contrib.auth.models import User


class Forum(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField('Createddate', auto_now_add=True)
    founder = models.ForeignKey(User)
    urlname = models.CharField(max_length=100, unique=True, default='')

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=61)
    forum = models.ForeignKey(Forum)
    date = models.DateField('session created date', auto_now_add=True)
    urlname = models.CharField(max_length=61, unique=True, default='')

    def __str__(self):
        return self.name


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=31)
    text = models.TextField()
    date = models.DateField('post date', auto_now_add=True)
    session = models.ForeignKey(Session)
    forum = models.ForeignKey(Forum)
    writer = models.ForeignKey(User)
    urlname = models.CharField(max_length=61, unique=True, default='')

    def __str__(self):
        return self.title


class Comment(models.Model):
    commenttext = models.TextField()
    date = models.DateField("comment", auto_now_add=True)
    post = models.ForeignKey(Post)
    writer = models.ForeignKey(User)

