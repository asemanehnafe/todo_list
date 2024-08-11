from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from todo_list.models import ToDoList


class AllTodoListsView(ListView, LoginRequiredMixin):
    model = ToDoList
    template_name = "todo_list_app/v2/todo_lists_v2.html"
    context_object_name = "todo_lists"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_lists"] = context["todo_lists"].filter(user=self.request.user)
        return context
