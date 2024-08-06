from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from todo_list_app.models import TaskLink, ToDoList
from todo_list_app.forms import CreateTaskByShortenLinkForm
from django.views.generic.edit import FormView


class CreateTaskByShortLinkView(FormView, LoginRequiredMixin):
    form_class = CreateTaskByShortenLinkForm
    template_name = 'todo_list_app/v1/create_task_view_v1.html'

    def get_success_url(self):
        list_id = self.kwargs['list_id']
        return reverse_lazy('tasks_view_v2', kwargs={'list_id': list_id})

    def form_valid(self, form):
        list_id = self.kwargs['list_id']
        short_link = get_object_or_404(TaskLink, uuid=form.cleaned_data['shorten_link'])
        new_task = short_link.task
        list_instance = ToDoList.objects.get(id=list_id)
        list_instance.tasks.add(new_task)
        x = super().form_valid(form)
        print(x)
        return x
