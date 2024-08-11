from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.models import Task


@method_decorator(login_required, name="dispatch")
class TodoListDetailView(View):
    def get(self, request, todo_list_id):
        tasks = Task.objects.filter(
            todolist__id=todo_list_id, todolist__user=request.user
        )
        return render(
            request,
            "todo_list_app/v2_2/todo_list_detail_v2_2.html",
            {"tasks": tasks, "todo_list_id": todo_list_id},
        )
