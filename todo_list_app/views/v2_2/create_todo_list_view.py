from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from todo_list_app.forms import TodoListForm


@method_decorator(login_required, name="dispatch")
class CreateTodoListView(View):
    form_class = TodoListForm
    template_name = ("todo_list_app/v1/create_list_view_v1.html")

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_todo_list = form.save(commit=False)
            new_todo_list.user = request.user
            new_todo_list.save()
            return redirect('all_todo_lists_view_v2_2')

        return render(request, self.template_name, {"form": form})
