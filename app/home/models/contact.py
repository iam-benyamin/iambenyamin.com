from django.db import models


class Contact(models.Model):
    number = models.IntegerField()
    email = models.EmailField(max_length=254)
    date = models.DateTimeField()
