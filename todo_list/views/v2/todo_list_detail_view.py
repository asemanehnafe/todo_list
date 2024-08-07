from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from todo_list.models import Task


class TodoListDetailView(ListView, LoginRequiredMixin):
    model = Task
    template_name = 'todo_list_app/v2/todo_list_detail_v2.html'
    context_object_name = 'todo_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = context['todo_list'].filter(todolist__id=self.kwargs['todo_list_id'],
                                                      todolist__user=self.request.user)
        context['todo_list_id'] = self.kwargs['todo_list_id']
        return context
