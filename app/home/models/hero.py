from django.db import models


class Hero(models.Model):
    header = models.CharField(max_length=50)
    text = models.CharField(max_length=120)
    thumbnail = models.ImageField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.header}, {self.text}"
