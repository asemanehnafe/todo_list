from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from todo_list_app.models import ToDoList
from todo_list_app.forms import ListForm


@login_required
def list_view(request):
    lists = ToDoList.objects.filter(user=request.user)
    return render(request, 'todo_list_app/v1/to_do_lists_view_v1.html', {'lists': lists})


@login_required
def create_list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user
            new_list.save()
            return redirect('all_lists_view_v1')
    else:
        form = ListForm()
    return render(request, './todo_list_app/v1/create_list_view_v1.html', {'form': form})


@login_required
def delete_list(request, list_id):
    deleting_list = get_object_or_404(ToDoList, id=list_id)
    deleting_list.delete()
    return redirect('all_lists_view_v1')
