from time import timezone

from django.db import models


class Todo_model(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Create your models here.

class Validation_model(models.Model):
    username = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    save = models.BooleanField(default=False)

    def __str__(self):
        return self.username



