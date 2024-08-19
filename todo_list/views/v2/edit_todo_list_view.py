from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from todo_list.forms import TodoListForm
from todo_list.models import ToDoList


class EditTodoListView(UpdateView, LoginRequiredMixin):
    model = ToDoList
    success_url = reverse_lazy("all_todo_lists_view_v2")
    template_name = "todo_list_app/form_display.html"
    form_class = TodoListForm
