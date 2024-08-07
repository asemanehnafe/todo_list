from django.contrib import admin
from .models.task import Task
from .models.to_do_list import ToDoList
from .models.task_link import TaskLink

admin.site.register(Task)
admin.site.register(ToDoList)
admin.site.register(TaskLink)
