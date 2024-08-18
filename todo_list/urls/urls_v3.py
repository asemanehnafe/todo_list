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
]
