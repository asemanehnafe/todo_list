from datetime import datetime

from django.db import models


class Task(models.Model):
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    PRIORITY_CHOICES = [
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    ]

    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    deadline = models.DateField(verbose_name="تاریخ سررسید", default=datetime.now)
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES, default=MEDIUM, verbose_name="الویت"
    )
    file = models.FileField(upload_to="task_files", blank=True, null=True)

    class Meta:
        ordering = ["deadline", "priority"]

    def __str__(self):
        return self.title
