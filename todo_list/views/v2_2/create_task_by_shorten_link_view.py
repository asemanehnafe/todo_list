from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.forms import CreateTaskByShortenLinkForm
from todo_list.models import TaskLink, ToDoList


@method_decorator(login_required, name="dispatch")
class CreateTaskByShortenLinkView(View):
    form_class = CreateTaskByShortenLinkForm
    template_name = "todo_list_app/create_task.html"

    def get(self, request, *args, **kwargs):
        form = CreateTaskByShortenLinkForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, todo_list_id):
        form = CreateTaskByShortenLinkForm(request.POST)
        if form.is_valid():
            short_link = get_object_or_404(
                TaskLink, uuid=form.cleaned_data["shorten_link"]
            )
            new_task = short_link.task
            todo_list_instance = ToDoList.objects.get(id=todo_list_id)
            todo_list_instance.tasks.add(new_task)
            return redirect("tasks_view_v2_2", todo_list_id=todo_list_id)
