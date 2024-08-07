from django.views import View
from todo_list.models import ToDoList, Task
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class DeleteTaskView(View):
    def get(self, request, todo_list_id, task_id):
        current_todo_list = get_object_or_404(ToDoList, id=todo_list_id)
        task = get_object_or_404(Task, id=task_id)
        current_todo_list.tasks.remove(task)
        if task.todolist_set.count() == 0:
            task.delete()
        return redirect('tasks_view_v2_2', todo_list_id=todo_list_id)
