from django.db import models

from ckeditor.fields import RichTextField


class CV(models.Model):
    slug = models.SlugField(max_length=200)
    body = RichTextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.slug
