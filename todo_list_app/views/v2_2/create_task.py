from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from todo_list_app.forms import TaskForm
from todo_list_app.models import ToDoList


@method_decorator(login_required, name="dispatch")
class CreateTask(View):
    form_class = TaskForm
    template_name = ("todo_list_app/v1/create_task_view_v1.html")

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, list_id):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.save()
            list_instance = ToDoList.objects.get(id=list_id)
            list_instance.tasks.add(new_task)
            return redirect('tasks_view_v2_2', list_id=list_id)

        return render(request, self.template_name, {"form": form})
