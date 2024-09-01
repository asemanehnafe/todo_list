from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.forms import TaskForm
from todo_list.models import Task, save_form_data_to_task_instance


@method_decorator(login_required, name="dispatch")
class EditTaskView(View):
    form_class = TaskForm
    template_name = "todo_list_app/form_display.html"

    def get(self, request, todo_list_id, task_id):
        form = TaskForm(instance=get_object_or_404(Task, id=task_id))
        return render(request, self.template_name, {"form": form, "title": "Edit Task"})

    def post(self, request, todo_list_id, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            save_form_data_to_task_instance(task, form)
            return redirect("tasks_view_v1", todo_list_id=todo_list_id)
        return render(request, self.template_name, {"form": form, "title": "Edit Task"})
