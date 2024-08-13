from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.models import ToDoList


@method_decorator(login_required, name="dispatch")
class DeleteTodoListView(View):
    def get(self, request, todo_list_id):
        deleting_todo_list = get_object_or_404(ToDoList, id=todo_list_id)
        for task in deleting_todo_list.tasks.all():
            if task.todolist_set.count() == 1:
                task.delete()
        deleting_todo_list.delete()
        return redirect("all_todo_lists_view_v2_2")