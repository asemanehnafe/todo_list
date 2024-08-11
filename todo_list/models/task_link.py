import uuid

from django.db import models


class TaskLink(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    task = models.ForeignKey(to="todo_list.Task", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uuid)
