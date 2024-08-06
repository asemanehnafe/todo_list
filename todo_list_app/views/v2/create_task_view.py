from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from todo_list_app.models import Task, ToDoList
from todo_list_app.forms import TaskForm


class CreateTaskView(CreateView, LoginRequiredMixin):
    model = Task
    form_class = TaskForm
    template_name = 'todo_list_app/v1/create_task_view_v1.html'

    def get_success_url(self):
        list_id = self.kwargs['list_id']
        return reverse_lazy('tasks_view_v2', kwargs={'list_id': list_id})

    def form_valid(self, form):
        task = form.save()
        list_id = self.kwargs.get('list_id')
        task_list = get_object_or_404(ToDoList, id=list_id)
        task_list.tasks.add(task)
        list_id = self.kwargs['list_id']
        print(list_id)
        return super(CreateTaskView, self).form_valid(form)
