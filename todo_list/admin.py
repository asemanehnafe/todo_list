from django.contrib import admin

from .models.task import Task
from .models.task_link import TaskLink
from .models.to_do_list import ToDoList

admin.site.register(Task)
admin.site.register(ToDoList)
admin.site.register(TaskLink)
