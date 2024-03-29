from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=120)
    country = models.CharField(max_length=80)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.address}, {self.country}"
