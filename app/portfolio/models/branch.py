from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=128)
    data_filter = models.CharField(
        max_length=128,
        help_text="change fild name space to hiphen",
    )
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"
