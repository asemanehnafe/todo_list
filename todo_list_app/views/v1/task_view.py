from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from todo_list_app.models import ToDoList, Task, TaskLink
from todo_list_app.forms import TaskForm
from todo_list_app.forms import CreateTaskByShortenLinkForm


@login_required
def task_view(request, todo_list_id):
    tasks = Task.objects.filter(todolist__id=todo_list_id, todolist__user=request.user)
    return render(request, 'todo_list_app/v1/tasks_view_v1.html', {'tasks': tasks, 'todo_list_id': todo_list_id})


@login_required
def create_task(request, todo_list_id):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.save()
            list_instance = ToDoList.objects.get(id=todo_list_id)
            list_instance.tasks.add(new_task)
            return redirect('tasks_view_v1', todo_list_id=todo_list_id)
    else:
        form = TaskForm()
    return render(request, 'todo_list_app/v1/create_task_view_v1.html', {'form': form})


@login_required
def create_task_by_shorten_link(request, todo_list_id):
    if request.method == 'POST':
        form = CreateTaskByShortenLinkForm(request.POST)
        if form.is_valid():
            short_link = get_object_or_404(TaskLink, uuid=form.cleaned_data['shorten_link'])
            new_task = short_link.task
            list_instance = ToDoList.objects.get(id=todo_list_id)
            list_instance.tasks.add(new_task)
            return redirect('tasks_view_v1', todo_list_id=todo_list_id)
    else:
        form = CreateTaskByShortenLinkForm()
    return render(request, 'todo_list_app/v1/create_task_view_v1.html', {'form': form})


@login_required
def generate_short_link(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    short_link, created = TaskLink.objects.get_or_create(task=task)
    return render(request, 'todo_list_app/v1/generate_short_link.html', {'short_link': short_link})


@login_required
def task_detail_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'todo_list_app/v1/task_detail_view_v1.html', {'task': task})


@login_required
def delete_task(request, todo_list_id, task_id):
    current_list = get_object_or_404(ToDoList, id=todo_list_id)
    task = get_object_or_404(Task, id=task_id)
    current_list.tasks.remove(task)
    if task.todolist_set.count() == 0:
        task.delete()
    return redirect('tasks_view_v1', todo_list_id=todo_list_id)
