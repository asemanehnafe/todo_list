from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from todo_list_app.models import Task


class ListDetailListView(ListView, LoginRequiredMixin):
    model = Task
    template_name = 'todo_list_app/v2/task_view_v2.html'
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = context['list'].filter(todolist__id=self.kwargs['list_id'], todolist__user=self.request.user)
        context['list_id'] = self.kwargs['list_id']
        return context
