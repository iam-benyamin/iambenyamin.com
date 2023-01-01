from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"
