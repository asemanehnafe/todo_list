import uuid
from django.db import models
from .task import Task


class ShortLink(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uuid)
