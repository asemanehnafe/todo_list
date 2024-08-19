import uuid

from django.core.exceptions import ValidationError
from django.db import models


def validate_uuid(value):
    try:
        uuid.UUID(str(value))
    except ValueError:
        raise ValidationError(f"{value} is not a valid UUID.")


class TaskLink(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="لینک کوتاه شده",
        validators=[validate_uuid],
    )
    task = models.ForeignKey(
        to="todo_list.Task", on_delete=models.CASCADE, verbose_name="نام وظیفه"
    )

    def __str__(self):
        return str(self.uuid)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(TaskLink, self).save(*args, **kwargs)
