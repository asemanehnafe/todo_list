from django.contrib.auth.models import User
from django.db import models


class ToDoList(models.Model):
    name = models.CharField(max_length=100, verbose_name="عنوان")
    tasks = models.ManyToManyField(
        to="todo_list.Task", blank=True, verbose_name="وظیفه ها"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")

    def __str__(self):
        return self.name
