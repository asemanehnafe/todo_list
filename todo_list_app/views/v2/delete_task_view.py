from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from todo_list_app.models import Task, ToDoList


class DeleteTaskView(DeleteView, LoginRequiredMixin):
    model = Task
    template_name = 'todo_list_app/v2/confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def delete(self, request, *args, **kwargs):
        todo_list_id = self.kwargs['list_id']
        current_list = get_object_or_404(ToDoList, id=todo_list_id)
        task = self.get_object()
        current_list.tasks.remove(task)
        if task.list_set.count() == 0:
            task.delete()

        return redirect('tasks_view_v1', todo_list_id=todo_list_id)

    def get_success_url(self):
        todo_list_id = self.kwargs['todo_list_id']
        return reverse_lazy('tasks_view_v2', kwargs={'todo_list_id': todo_list_id})