from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from todo_list.models import ToDoList


class DeleteTodoListView(DeleteView, LoginRequiredMixin):
    model = ToDoList
    success_url = reverse_lazy("all_todo_lists_view_v2")
    template_name = "todo_list_app/v2/confirm_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
