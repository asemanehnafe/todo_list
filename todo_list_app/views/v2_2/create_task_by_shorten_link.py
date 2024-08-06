from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from todo_list_app.forms import CreateTaskByShortenLinkForm
from todo_list_app.models import ToDoList, TaskLink


@method_decorator(login_required, name="dispatch")
class CreateTaskByShortenLink(View):
    form_class = CreateTaskByShortenLinkForm
    template_name = ("todo_list_app/v1/create_task_view_v1.html")

    def get(self, request, *args, **kwargs):
        form = CreateTaskByShortenLinkForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, list_id):
        form = CreateTaskByShortenLinkForm(request.POST)
        if form.is_valid():
            short_link = get_object_or_404(TaskLink, uuid=form.cleaned_data['shorten_link'])
            new_task = short_link.task
            list_instance = ToDoList.objects.get(id=list_id)
            list_instance.tasks.add(new_task)
            return redirect('tasks_view_v2_2', list_id=list_id)
