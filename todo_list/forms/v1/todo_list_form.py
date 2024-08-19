from django import forms

from todo_list.models.to_do_list import *


class TodoListForm(forms.Form):
    name = forms.CharField(label="عنوان", required=True, validators=name_validators)
