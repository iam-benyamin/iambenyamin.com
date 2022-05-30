from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=120)
    thumbnail = models.ImageField()
    discription = models.CharField(max_length=355)
    body = RichTextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

