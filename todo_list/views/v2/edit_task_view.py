from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from todo_list.forms import TaskForm
from todo_list.models import Task


class EditTaskView(UpdateView, LoginRequiredMixin):
    model = Task
    template_name = "todo_list_app/create_task.html"
    form_class = TaskForm

    def get_success_url(self):
        todo_list_id = self.kwargs["todo_list_id"]
        return reverse_lazy("tasks_view_v2", kwargs={"todo_list_id": todo_list_id})
