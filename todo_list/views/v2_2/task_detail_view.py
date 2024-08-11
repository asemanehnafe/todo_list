from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.models import Task


@method_decorator(login_required, name="dispatch")
class TaskDetailView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        return render(request, "todo_list_app/v1/task_detail.html", {"task": task})
