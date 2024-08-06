from django.urls import path
from todo_list_app.views.v1 import *

urlpatterns = [
    path('', list_view, name='all_lists_view_v1'),
    path('create_list/', create_list, name='create_list_v1'),
    path('list/<int:list_id>/delete_list/', delete_list, name='delete_list_v1'),
    path('list/<int:list_id>/', task_view, name='tasks_view_v1'),
    path('list/<int:list_id>/create_task/', create_task, name='create_task_v1'),
    path('list/<int:list_id>/create_task_by_shortned_link/', create_task_by_shorten_link,
         name='create_task_by_shortened_link_v1'),
    path('task/<int:task_id>/generate_short_link/', generate_short_link, name='generate_short_link'),
    path('task/<int:task_id>/', task_detail_view, name='task_detail_view'),
    path('list/<int:list_id>/task/<int:task_id>/delete_task', delete_task, name='delete_task'),

]
