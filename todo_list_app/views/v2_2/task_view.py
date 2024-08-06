from django.views import View
from todo_list_app.models import Task
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class TaskView(View):
    def get(self, request, list_id):
        tasks = Task.objects.filter(todolist__id=list_id, todolist__user=request.user)
        return render(request, 'todo_list_app/v2_2/task_view_v2_2.html',
                      {'tasks': tasks, 'list_id': list_id})
