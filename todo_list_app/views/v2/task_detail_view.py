from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from todo_list_app.models import Task


class TaskDetailView(DetailView, LoginRequiredMixin):
    model = Task
    template_name = 'todo_list_app/v1/task_detail_view_v1.html'
    context_object_name = 'task'
