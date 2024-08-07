from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from todo_list_app.models import TaskLink, ToDoList
from todo_list_app.forms import CreateTaskByShortenLinkForm
from django.views.generic.edit import FormView


class CreateTaskByShortLinkView(FormView, LoginRequiredMixin):
    form_class = CreateTaskByShortenLinkForm
    template_name = 'todo_list_app/v1/create_task.html'

    def get_success_url(self):
        todo_list_id = self.kwargs['todo_list_id']
        return reverse_lazy('tasks_view_v2', kwargs={'todo_list_id': todo_list_id})

    def form_valid(self, form):
        todo_list_id = self.kwargs['todo_list_id']
        short_link = get_object_or_404(TaskLink, uuid=form.cleaned_data['shorten_link'])
        new_task = short_link.task
        todo_list_instance = ToDoList.objects.get(id=todo_list_id)
        todo_list_instance.tasks.add(new_task)
        return super().form_valid(form)
