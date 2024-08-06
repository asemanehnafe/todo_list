from django import forms
from todo_list_app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority']


class ShortenLinkTaskForm(forms.Form):
    shorten_link = forms.CharField(label='shorten link')
