from django.db import models


class ConnectMe(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, {self.subject}"
