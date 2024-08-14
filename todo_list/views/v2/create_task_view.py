from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from todo_list.forms import TaskForm
from todo_list.models import Task, ToDoList


class CreateTaskView(CreateView, LoginRequiredMixin):
    model = Task
    form_class = TaskForm
    template_name = "todo_list_app/create_task.html"

    def get_success_url(self):
        list_id = self.kwargs["todo_list_id"]
        return reverse_lazy("tasks_view_v2", kwargs={"todo_list_id": list_id})

    def form_valid(self, form):
        task = form.save()
        todo_list_id = self.kwargs.get("todo_list_id")
        task_list = get_object_or_404(ToDoList, id=todo_list_id)
        task_list.tasks.add(task)
        return super(CreateTaskView, self).form_valid(form)
