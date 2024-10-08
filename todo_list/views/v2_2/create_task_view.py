from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.forms import TaskForm
from todo_list.models import ToDoList


@method_decorator(login_required, name="dispatch")
class CreateTaskView(View):
    form_class = TaskForm
    template_name = "todo_list_app/form_display.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request, self.template_name, {"form": form, "title": "Create Task"}
        )

    def post(self, request, todo_list_id):
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.save()
            todo_list_instance = ToDoList.objects.get(id=todo_list_id)
            todo_list_instance.tasks.add(new_task)
            return redirect("tasks_view_v2_2", todo_list_id=todo_list_id)

        return render(
            request, self.template_name, {"form": form, "title": "Create Task"}
        )
