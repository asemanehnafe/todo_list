from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from todo_list.forms import TodoListForm
from todo_list.models import ToDoList
from django.views.generic.edit import CreateView


class CreateTodoListView(CreateView, LoginRequiredMixin):
    model = ToDoList
    success_url = reverse_lazy('all_todo_lists_view_v2')
    template_name = 'todo_list_app/v1/create_todo_list.html'
    form_class = TodoListForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTodoListView, self).form_valid(form)
