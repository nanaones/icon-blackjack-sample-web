from django.db import models
from django.utils import timezone

import iconsdk.icon_service
from iconsdk.builder.call_builder import CallBuilder


# class Post(models.Model):
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title


class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField(max_length=50)
    url = models.URLField()
    email = models.EmailField()
    # cdate = models.DateTimeField(auto_created=True)


class Network(models.Model):
    url = models.URLField()


class Makegameroom(models.Model):
    useraddress = models.CharField(max_length=50)
    prize_per_game = models.CharField(max_length=50)

