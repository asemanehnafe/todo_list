from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo_list.models import ToDoList
from todo_list.serializer import TodoListSerializer

ONE = 1


class TodoListModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDoList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        for task in instance.tasks.all():
            is_task_only_in_this_list = task.todolist_set.count() == ONE
            if is_task_only_in_this_list:
                task.delete()
        instance.delete()
