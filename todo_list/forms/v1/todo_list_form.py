from django import forms


class TodoListForm(forms.Form):
    name = forms.CharField(
        label="عنوان",
        required=True,
    )
