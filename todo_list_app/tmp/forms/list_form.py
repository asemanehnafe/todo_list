from django import forms
from todo_list_app.models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name']