from django import forms
from todo_list_app.models import ToDoList


class ListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['name']