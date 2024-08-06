from django.urls import path
from todo_list_app.views.v2 import *

urlpatterns = [

    path('', AllListListView.as_view(), name='all_lists_view_v2'),
    path('create_list/', CreateListView.as_view(), name='create_list_v2'),
    path('list/<int:pk>/delete_list/', DeleteListView.as_view(), name='delete_list_v2'),
    path('list/<int:list_id>/', ListDetailListView.as_view(), name='tasks_view_v2'),
    path('list/<int:list_id>/create_task/', CreateTaskView.as_view(), name='create_task_v2'),
    path('list/<int:list_id>/create_task_by_shortned_link/', CreateTaskByShortLinkView.as_view(),
         name='create_task_by_shortened_link_v2'),
    path('task/<int:task_id>/generate_short_link/', GenerateShortLink.as_view(), name='generate_short_link_v2'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail_view_v2'),
    path('list/<int:list_id>/task/<int:pk>/delete_task', DeleteTaskView.as_view(), name='delete_task_v2'),
]