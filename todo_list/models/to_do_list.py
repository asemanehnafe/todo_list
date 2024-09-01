from django.contrib.auth.models import User
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from todo_list.utils import invalid_todo_list_cache

name_validators = [
    MinLengthValidator(1, message="The title must be at least 1 characters long."),
    MaxLengthValidator(100, message="The title must be at least 255 characters long."),
    RegexValidator(
        regex=r"^[\w\s]+$",
        message="The title can only contain letters, numbers, and spaces.",
        code="invalid_title",
    ),
]


class ToDoList(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="عنوان", validators=name_validators
    )
    tasks = models.ManyToManyField(
        to="todo_list.Task", blank=True, verbose_name="وظیفه ها"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ToDoList, self).save(*args, **kwargs)


@receiver(post_save, sender=ToDoList)
def invalid_todo_list_cache_post_save(sender, instance, **kwargs):
    invalid_todo_list_cache(instance.user.id)
