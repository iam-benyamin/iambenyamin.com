from django.db import models


class Link(models.Model):
    title = models.CharField(max_length=50)
    links = models.URLField()
    color = models.CharField(max_length=8)
    discription = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.title