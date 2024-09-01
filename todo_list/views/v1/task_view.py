from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from todo_list.forms import CreateTaskByShortenLinkForm
from todo_list.forms.v1 import TaskForm
from todo_list.models import Task, TaskLink, ToDoList, save_form_data_to_task_instance

ZERO = 0


@login_required
def task_view(request, todo_list_id):
    tasks = Task.objects.filter(todolist__id=todo_list_id, todolist__user=request.user)

    return render(
        request,
        "todo_list_app/v1/todo_list_detail_v1.html",
        {"tasks": tasks, "todo_list_id": todo_list_id},
    )


@login_required
def create_task(request, todo_list_id):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            new_task = Task(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                deadline=form.cleaned_data["deadline"],
                priority=form.cleaned_data["priority"],
                file=form.cleaned_data["file"],
            )
            new_task.save()
            list_instance = ToDoList.objects.get(id=todo_list_id)
            list_instance.tasks.add(new_task)
            return redirect("tasks_view_v1", todo_list_id=todo_list_id)
    else:
        form = TaskForm()
    return render(
        request,
        "todo_list_app/v1/task_edits_v1.html",
        {"form": form, "title": "Create Task"},
    )


@login_required
def create_task_by_shorten_link(request, todo_list_id):
    if request.method == "POST":
        form = CreateTaskByShortenLinkForm(request.POST)
        if form.is_valid():
            short_link = get_object_or_404(
                TaskLink, uuid=form.cleaned_data["shorten_link"]
            )
            new_task = short_link.task
            list_instance = ToDoList.objects.get(id=todo_list_id)
            list_instance.tasks.add(new_task)
            return redirect("tasks_view_v1", todo_list_id=todo_list_id)
    else:
        form = CreateTaskByShortenLinkForm()
    return render(
        request,
        "todo_list_app/form_display.html",
        {"form": form, "title": "create task by short link"},
    )


@login_required
def generate_short_link(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    short_link, created = TaskLink.objects.get_or_create(task=task)
    return render(
        request,
        "todo_list_app/generate_short_link.html",
        {"short_link": short_link},
    )


@login_required
def task_detail_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(
        request,
        "todo_list_app/task_detail.html",
        {"task": task},
    )


@login_required
def delete_task(request, todo_list_id, task_id):
    current_list = get_object_or_404(ToDoList, id=todo_list_id)
    task = get_object_or_404(Task, id=task_id)
    current_list.tasks.remove(task)
    is_task_in_no_list = task.todolist_set.count() == ZERO
    if is_task_in_no_list:
        task.delete()
    return redirect("tasks_view_v1", todo_list_id=todo_list_id)


@login_required
def edit_task(request, todo_list_id, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid():
            save_form_data_to_task_instance(task, form)
            return redirect("tasks_view_v1", todo_list_id=todo_list_id)
    else:
        form = TaskForm(
            initial={
                "title": task.title,
                "description": task.description,
                "deadline": task.deadline,
                "priority": task.priority,
                "file": task.file,
            }
        )
    return render(
        request,
        "todo_list_app/v1/task_edits_v1.html",
        {"form": form, "title": "Edit Task"},
    )
