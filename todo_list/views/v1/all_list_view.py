from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from todo_list.forms.v1 import TodoListForm
from todo_list.models import ToDoList

ONE = 1


@login_required
def todo_list_view(request):
    todo_lists = ToDoList.objects.filter(user=request.user)
    return render(
        request, "todo_list_app/v1/todo_lists_v1.html", {"todo_lists": todo_lists}
    )


@login_required
def create_todo_list(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            new_todo_list = ToDoList(name=form.cleaned_data["name"])
            new_todo_list.user = request.user
            new_todo_list.save()
            return redirect("all_todo_lists_view_v1")
    else:
        form = TodoListForm()
    return render(
        request,
        "todo_list_app/v1/todo_list_edits_v1.html",
        {"form": form, "title": "Create New TodoList"},
    )


@login_required
def delete_todo_list(request, todo_list_id):
    deleting_todo_list = get_object_or_404(ToDoList, id=todo_list_id)
    for task in deleting_todo_list.tasks.all():
        is_task_only_in_this_list = task.todolist_set.count() == ONE
        if is_task_only_in_this_list:
            task.delete()
    deleting_todo_list.delete()
    return redirect("all_todo_lists_view_v1")


def edit_todo_list(request, todo_list_id):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            editing_todo_list = get_object_or_404(ToDoList, id=todo_list_id)
            editing_todo_list.name = form.cleaned_data["name"]
            editing_todo_list.save()
            return redirect("all_todo_lists_view_v1")
    else:
        form = TodoListForm()
    return render(
        request,
        "todo_list_app/v1/todo_list_edits_v1.html",
        {"form": form, "title": "Edit todo_list"},
    )
