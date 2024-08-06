import uuid

from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    priority = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['deadline', 'priority']
