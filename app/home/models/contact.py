from django.db import models


class Contact(models.Model):
    number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    date = models.DateTimeField()
