from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from todo_list_app.forms import ListForm


@method_decorator(login_required, name="dispatch")
class CreateList(View):
    form_class = ListForm
    template_name = ("todo_list_app/v1/create_list_view_v1.html")

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user
            new_list.save()
            return redirect('all_lists_view_v2_2')

        return render(request, self.template_name, {"form": form})
