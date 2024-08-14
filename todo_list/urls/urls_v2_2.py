from django.urls import path

from todo_list.views.v2_2 import *

urlpatterns = [
    path("", AllTodoListsView.as_view(), name="all_todo_lists_view_v2_2"),
    path("create_todo_list/", CreateTodoListView.as_view(), name="create_list_v2_2"),
    path(
        "todo_list/<int:todo_list_id>/delete_todo_list/",
        DeleteTodoListView.as_view(),
        name="delete_todo_list_v2_2",
    ),
    path(
        "todo_list/<int:todo_list_id>/edit_todo_list/",
        EditTodoListView.as_view(),
        name="edit_todo_list_v2_2",
    ),
    path(
        "todo_list/<int:todo_list_id>/",
        TodoListDetailView.as_view(),
        name="tasks_view_v2_2",
    ),
    path(
        "todo_list/<int:todo_list_id>/create_task/",
        CreateTaskView.as_view(),
        name="create_task_v2_2",
    ),
    path(
        "todo_list/<int:todo_list_id>/create_task_by_shortned_link/",
        CreateTaskByShortenLinkView.as_view(),
        name="create_task_by_shortened_link_v2_2",
    ),
    path(
        "task/<int:task_id>/generate_short_link/",
        GenerateShortLinkView.as_view(),
        name="generate_short_link_v2_2",
    ),
    path("task/<int:task_id>/", TaskDetailView.as_view(), name="task_detail_view_v2_2"),
    path(
        "todo_list/<int:todo_list_id>/task/<int:task_id>/delete_task",
        DeleteTaskView.as_view(),
        name="delete_task_v2_2",
    ),
    path(
        "todo_list/<int:todo_list_id>/task/<int:task_id>/edit_task",
        EditTaskView.as_view(),
        name="edit_task_v2_2",
    ),
]
