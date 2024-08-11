from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from todo_list.models import Task


class TaskDetailView(DetailView, LoginRequiredMixin):
    model = Task
    template_name = "todo_list_app/v1/task_detail.html"
    context_object_name = "task"
