from django import forms


class TaskForm(forms.Form):
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    PRIORITY_CHOICES = [
        (HIGH, "High"),
        (MEDIUM, "Medium"),
        (LOW, "Low"),
    ]

    title = forms.CharField(
        label="عنوان",
        required=True,
    )
    description = forms.CharField(
        label="توضیحات", widget=forms.Textarea, required=False
    )
    deadline = forms.DateField(label="تاریخ سررسید")
    priority = forms.ChoiceField(label="الویت", choices=PRIORITY_CHOICES)
    file = forms.FileField(required=False)
