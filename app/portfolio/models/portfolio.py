from django.db import models

from ckeditor.fields import RichTextField


class Portfolio(models.Model):
    iamge = models.ImageField()
    title = models.CharField(max_length=80)
    short_description = models.CharField(max_length=255)
    description = RichTextField()
    customer_opinion = models.CharField(max_length=300)
    branch = models.ForeignKey(
        'portfolio.Branch',
        null=True,
        on_delete=models.SET_NULL
    )
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.title}"
