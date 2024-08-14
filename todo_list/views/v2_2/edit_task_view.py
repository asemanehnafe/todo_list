from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.forms import TaskForm
from todo_list.models import Task


@method_decorator(login_required, name="dispatch")
class EditTaskView(View):
    def get(self, request, todo_list_id, task_id):
        form = TaskForm()
        return render(
            request,
            "todo_list_app/v1/task_edits_v1.html",
            {"form": form, "title": "Edit Task"},
        )

    def post(self, request, todo_list_id, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task.title = form.cleaned_data["title"]
            task.description = form.cleaned_data["description"]
            task.deadline = form.cleaned_data["deadline"]
            task.priority = form.cleaned_data["priority"]
            task.file = form.cleaned_data["file"]
            task.save()
            return redirect("tasks_view_v1", todo_list_id=todo_list_id)