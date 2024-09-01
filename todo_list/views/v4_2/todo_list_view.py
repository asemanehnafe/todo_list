from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo_list.models import ToDoList
from todo_list.serializer import TodoListSerializer
from todo_list.utils import todo_list_cache_key

TASK_COUNT_IN_LIST = 1


class TodoListModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]

    # @method_decorator(
    #     cache_page(3600 * 24, key_prefix="todo_list_view", key_func=todo_list_cache_key)
    # )
    def get_queryset(self):
        print("get_queryset called")
        return ToDoList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        for task in instance.tasks.all():
            if task.todolist_set.count() == TASK_COUNT_IN_LIST:
                task.delete()
        instance.delete()
