from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.models import Task, ToDoList

ZERO = 0


@method_decorator(login_required, name="dispatch")
class DeleteTaskView(View):
    def get(self, request, todo_list_id, task_id):
        current_todo_list = get_object_or_404(ToDoList, id=todo_list_id)
        task = get_object_or_404(Task, id=task_id)
        current_todo_list.tasks.remove(task)
        is_task_in_no_list = task.todolist_set.count() == ZERO
        if is_task_in_no_list:
            task.delete()
        return redirect("tasks_view_v2_2", todo_list_id=todo_list_id)
