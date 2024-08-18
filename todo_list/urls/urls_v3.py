from django.urls import path

from todo_list.views.v3 import *

urlpatterns = [
    path("", AllTodoListsView.as_view(), name="all_todo_lists_view_v3"),
    path(
        "todo_list/<int:pk>/edit_todo_list/",
        EditTodoListView.as_view(),
        name="edit_todo_list_v3",
    ),
    path(
        "todo_list/<int:pk>/delete_todo_list/",
        DeleteTodoListView.as_view(),
        name="delete_todo_list_v3",
    ),
    path("create_todo_list/", CreateTodoListView.as_view(), name="create_list_v3"),
    path(
        "todo_list/<int:todo_list_id>/",
        TodoListDetailView.as_view(),
        name="tasks_view_v3",
    ),
    path(
        "todo_list/<int:todo_list_id>/create_task/",
        CreateTaskView.as_view(),
        name="create_task_v3",
    ),
    path(
        "todo_list/<int:todo_list_id>/task/<int:pk>/delete_task/",
        DeleteTaskView.as_view(),
        name="delete_task_v3",
    ),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task_detail_view_v3"),
    path(
        "todo_list/<int:todo_list_id>/task/<int:pk>/edit_task/",
        EditTaskView.as_view(),
        name="edit_task_v3",
    ),
]
