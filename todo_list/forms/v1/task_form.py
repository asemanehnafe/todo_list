from django import forms

from todo_list.models.task import *


class TaskForm(forms.Form):
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    PRIORITY_CHOICES = [
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    ]

    title = forms.CharField(label="عنوان", required=True, validators=title_validators)
    description = forms.CharField(
        label="توضیحات",
        widget=forms.Textarea,
        required=False,
        validators=description_validators,
    )
    deadline = forms.DateField(label="تاریخ سررسید", validators=[deadline_validator])
    priority = forms.ChoiceField(
        label="الویت", choices=PRIORITY_CHOICES, validators=[priority_validator]
    )
    file = forms.FileField(required=False, validators=[validate_file_extension])
