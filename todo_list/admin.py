from django.contrib import admin

from .models.task import Task
from .models.task_link import TaskLink
from .models.to_do_list import ToDoList

main_admins = ["asemaneh"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "deadline", "priority", "file")
    readonly_fields = ["id"]
    search_fields = ("title", "priority")

    # list_filter = ("completed",)

    def has_add_permission(self, request):
        if request.user.username in main_admins:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.username in main_admins:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username in main_admins:
            return True
        return False


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ["name"]
    readonly_fields = ["id"]
    search_fields = ["name"]

    def has_add_permission(self, request):
        if request.user.username in main_admins:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.username in main_admins:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username in main_admins:
            return True
        return False


@admin.register(TaskLink)
class TaskLinkAdmin(admin.ModelAdmin):
    list_display = ["uuid", "task"]
    search_fields = ["uuid", "task"]

    def has_add_permission(self, request):
        if request.user.username in main_admins:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.username in main_admins:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username in main_admins:
            return True
        return False
