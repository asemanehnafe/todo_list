from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.forms.to_do_list_form import TodoListForm
from todo_list.models import ToDoList


@method_decorator(login_required, name="dispatch")
class EditTodoListView(View):
    template_name = "todo_list_app/create_todo_list.html"

    def get(self, request, todo_list_id):
        form = TodoListForm()
        return render(
            request,
            self.template_name,
            {"form": form, "title": "Edit todo_list"},
        )

    def post(self, request, todo_list_id):
        form = TodoListForm(request.POST)
        if form.is_valid():
            editing_todo_list = get_object_or_404(ToDoList, id=todo_list_id)
            editing_todo_list.name = form.cleaned_data["name"]
            editing_todo_list.save()
            return redirect("all_todo_lists_view_v1")
