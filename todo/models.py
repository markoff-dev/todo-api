from django.contrib.auth import get_user_model
from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    due = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title