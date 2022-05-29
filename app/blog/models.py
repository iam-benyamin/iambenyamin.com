from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=120)
    discription = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
