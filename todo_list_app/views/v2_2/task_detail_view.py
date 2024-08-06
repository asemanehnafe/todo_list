from django.views import View
from todo_list_app.models import Task
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class TaskDetailView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        return render(request, 'todo_list_app/v1/task_detail_view_v1.html', {'task': task})
