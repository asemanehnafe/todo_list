from django.contrib.auth.models import User
from django.db import models


class ToDoList(models.Model):
    name = models.CharField(max_length=100)
    tasks = models.ManyToManyField(to="todo_list_app.Task", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
