from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from todo_list_app.forms import ListForm
from todo_list_app.models import ToDoList
from django.views.generic.edit import CreateView


class CreateListView(CreateView, LoginRequiredMixin):
    model = ToDoList
    success_url = reverse_lazy('all_lists_view_v2')
    template_name = 'todo_list_app/v1/create_list_view_v1.html'
    form_class = ListForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateListView, self).form_valid(form)
