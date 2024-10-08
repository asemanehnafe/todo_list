from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.forms import TodoListForm


@method_decorator(login_required, name="dispatch")
class CreateTodoListView(View):
    form_class = TodoListForm
    template_name = "todo_list_app/form_display.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            new_todo_list = form.save(commit=False)
            new_todo_list.user = request.user
            new_todo_list.save()
            return redirect("all_todo_lists_view_v2_2")

        return render(request, self.template_name, {"form": form})
