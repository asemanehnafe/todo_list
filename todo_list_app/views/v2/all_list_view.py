from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from todo_list_app.models import ToDoList


class AllListListView(ListView, LoginRequiredMixin):
    model = ToDoList
    template_name = 'todo_list_app/v2/todo_lists.html'
    context_object_name = 'lists_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists_list'] = context['lists_list'].filter(user=self.request.user)
        return context




