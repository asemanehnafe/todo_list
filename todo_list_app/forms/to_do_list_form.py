from django import forms
from todo_list_app.models import ToDoList


class TodoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['name']