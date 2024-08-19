import datetime
import os

from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, RegexValidator
from django.db import models
from django.utils import timezone


def title_validator(value):
    if value is None or value == "":
        raise ValidationError(
            "%(value)can not be empty",
            params={"value": value},
        )
    if len(value) > 100:
        raise ValidationError(
            "%(value)can not be longer than 100 characters", params={"value": value}
        )


title_validators = [
    title_validator,
    RegexValidator(
        regex=r"^[\w\s]+$",
        message="The title can only contain letters, numbers, and spaces.",
        code="invalid_title",
    ),
]

description_validators = [
    MaxLengthValidator(
        600, message="The description must be at least 600 characters long."
    )
]


def deadline_validator(value):
    if value < timezone.now().date():
        raise ValidationError("The deadline cannot be in the past.")


def priority_validator(value):
    value = int(value)
    if value not in [1, 2, 3]:
        raise ValidationError(
            "%(value)s is not in valid priority range",
            params={"value": value},
        )


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".pdf", ".doc", ".docx", ".txt"]
    if ext.lower() not in valid_extensions:
        raise ValidationError("Unsupported file extension.")


class Task(models.Model):
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    PRIORITY_CHOICES = [
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    ]

    title = models.CharField(
        max_length=100,
        verbose_name="عنوان",
        validators=title_validators,
    )
    description = models.TextField(
        verbose_name="توضیحات",
        validators=description_validators,
    )

    deadline = models.DateField(
        verbose_name="تاریخ سررسید",
        default=datetime.date.today,
        validators=[deadline_validator],
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=MEDIUM,
        verbose_name="الویت",
        validators=[priority_validator],
    )
    file = models.FileField(
        upload_to="task_files",
        blank=True,
        null=True,
        validators=[validate_file_extension],
    )

    class Meta:
        ordering = ["deadline", "priority"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.clean()
        return super(Task, self).save(*args, **kwargs)
