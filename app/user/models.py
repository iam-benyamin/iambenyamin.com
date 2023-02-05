from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser): ...


class Subscriber(models.Model):
    email = models.EmailField(max_length=254)
    date_of_subscribe = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}"
