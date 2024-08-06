from django.views import View
from todo_list_app.models import ToDoList
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class DeleteList(View):
    def get(self, request, list_id):
        deleting_list = get_object_or_404(ToDoList, id=list_id)
        deleting_list.delete()
        return redirect('all_lists_view_v2_2')

