from django.urls import path
from todo_list_app.views.v1 import *

urlpatterns = [
    path('', todo_list_view, name='all_todo_lists_view_v1'),
    path('create_todo_list/', create_todo_list, name='create_todo_list_v1'),
    path('todo_list/<int:todo_list_id>/delete_todo_list/', delete_todo_list, name='delete_todo_list_v1'),
    path('todo_list/<int:todo_list_id>/', task_view, name='tasks_view_v1'),
    path('todo_list/<int:todo_list_id>/create_task/', create_task, name='create_task_v1'),
    path('todo_list/<int:todo_list_id>/create_task_by_shortned_link/', create_task_by_shorten_link,
         name='create_task_by_shortened_link_v1'),
    path('task/<int:task_id>/generate_short_link/', generate_short_link, name='generate_short_link'),
    path('task/<int:task_id>/', task_detail_view, name='task_detail_view'),
    path('todo_list/<int:todo_list_id>/task/<int:task_id>/delete_task', delete_task, name='delete_task'),

]
