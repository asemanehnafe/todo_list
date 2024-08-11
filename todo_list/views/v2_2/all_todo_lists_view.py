from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.models import ToDoList


@method_decorator(login_required, name="dispatch")
class AllTodoListsView(View):
    def get(self, request):
        todo_lists = ToDoList.objects.filter(user=request.user)
        return render(
            request,
            "todo_list_app/v2_2/todo_lists_v2_2.html",
            {"todo_lists": todo_lists},
        )
