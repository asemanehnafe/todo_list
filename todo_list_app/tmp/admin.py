from django.contrib import admin
from .models.task import Task
from .models.list import List

admin.site.register(Task)
admin.site.register(List)
