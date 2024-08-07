from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from todo_list.models import ToDoList
from todo_list.forms import TodoListForm


@login_required
def todo_list_view(request):
    todo_lists = ToDoList.objects.filter(user=request.user)
    return render(request, 'todo_list_app/v1/todo_lists_v1.html', {'todo_lists': todo_lists})


@login_required
def create_todo_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            new_todo_list = form.save(commit=False)
            new_todo_list.user = request.user
            new_todo_list.save()
            return redirect('all_todo_lists_view_v1')
    else:
        form = TodoListForm()
    return render(request, './todo_list_app/v1/create_todo_list.html', {'form': form})


@login_required
def delete_todo_list(request, todo_list_id):
    deleting_todo_list = get_object_or_404(ToDoList, id=todo_list_id)
    deleting_todo_list.delete()
    return redirect('all_todo_lists_view_v1')
