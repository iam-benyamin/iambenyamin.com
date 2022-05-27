from django.db import models


class Video(models.Model):
    thumbnail = models.ImageField()
    video = models.FileField()
    date = models.DateTimeField()
