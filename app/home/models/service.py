from django.db import models


class Service(models.Model):
    icone = models.CharField(max_length=255)
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=150)
    date = models.DateTimeField()
