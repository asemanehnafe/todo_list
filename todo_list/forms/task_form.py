from django import forms
from todo_list.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority']


class CreateTaskByShortenLinkForm(forms.Form):
    shorten_link = forms.CharField(label='shorten link')
