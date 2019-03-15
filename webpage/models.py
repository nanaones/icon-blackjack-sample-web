from django.db import models


# class Article(models.Model):
#     name = models.CharField(max_length=50)
#     title = models.CharField(max_length=50)
#     contents = models.TextField(max_length=50)
#     url = models.URLField()
#     email = models.EmailField()
    # cdate = models.DateTimeField(auto_created=True)


class MakeGameRoom(models.Model):
    game_room_address = models.CharField(max_length=50)


