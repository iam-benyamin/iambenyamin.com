from django.db import models


class Contact(models.Model):
    number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.number}, {self.email}"