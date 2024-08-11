from django import forms

from todo_list.models import ToDoList


class TodoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ["name"]
