from django.urls import path
from todo_list_app.views.v2_2 import *

urlpatterns = [
    path('', AllListView.as_view(), name='all_lists_view_v2_2'),
    path('create_list/', CreateList.as_view(), name='create_list_v2_2'),
    path('list/<int:list_id>/delete_list/', DeleteList.as_view(), name='delete_list_v2_2'),
    path('list/<int:list_id>/', TaskView.as_view(), name='tasks_view_v2_2'),
    path('list/<int:list_id>/create_task/', CreateTask.as_view(), name='create_task_v2_2'),
    path('list/<int:list_id>/create_task_by_shortned_link/', CreateTaskByShortenLink.as_view(),
         name='create_task_by_shortened_link_v2_2'),
    path('task/<int:task_id>/generate_short_link/', GenerateShortLink.as_view(), name='generate_short_link_v2_2'),
    path('task/<int:task_id>/', TaskDetailView.as_view(), name='task_detail_view_v2_2'),
    path('list/<int:list_id>/task/<int:task_id>/delete_task', DeleteTask.as_view(), name='delete_task_v2_2'),

]
