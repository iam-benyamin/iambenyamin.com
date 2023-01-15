from django.db import models


class MyStory(models.Model):
    who_i_am = models.TextField(max_length=490)
    my_vision = models.TextField(max_length=490)
    my_history = models.TextField(max_length=490)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.who_i_am[:20]}, {self.my_history[:20]}, {self.my_vision[:20]}"