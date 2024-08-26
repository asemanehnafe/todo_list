from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework import exceptions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from todo_list.models import Task, TaskLink, ToDoList
from todo_list.serializer import TaskLinkSerializer
from todo_list.serializer.v4_2 import TaskSerializer

ZERO = 0


class TaskModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ["generate_short_link", "create_task_by_shorten_link"]:
            return TaskLinkSerializer
        return TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(todolist__user=self.request.user)

    def perform_destroy(self, instance):
        if "todo_list_id" not in self.request.POST:
            raise exceptions.ValidationError({"todo_list_id": "is required"})
        todo_list_id = self.request.POST["todo_list_id"]
        current_list = get_object_or_404(ToDoList, id=todo_list_id)
        task = self.get_object()
        current_list.tasks.remove(task)
        is_task_in_no_list = task.todolist_set.count() == ZERO
        if is_task_in_no_list:
            task.delete()

    @action(detail=True, methods=["post"])
    def generate_short_link(self, request, pk=None):
        task = get_object_or_404(Task, id=pk)
        short_link, created = TaskLink.objects.get_or_create(task=task)
        serializer = self.get_serializer(short_link)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def create_task_by_shorten_link(self, request):
        if "todo_list_id" not in self.request.POST:
            raise exceptions.ValidationError({"todo_list_id": "is required"})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        short_link = get_object_or_404(TaskLink, uuid=serializer.validated_data["uuid"])
        new_task = short_link.task
        list_instance = ToDoList.objects.get(id=self.request.POST["todo_list_id"])
        list_instance.tasks.add(new_task)
        return Response(status=status.HTTP_201_CREATED)
