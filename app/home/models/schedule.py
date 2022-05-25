from django.db import models


class Schedule(models.Model):
    days = models.CharField(max_length=120)
    time = models.CharField(max_length=120)
    date = models.DateTimeField()
