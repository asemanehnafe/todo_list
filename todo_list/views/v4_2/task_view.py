from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from todo_list.models import Task, TaskLink, ToDoList
from todo_list.serializer import TaskSerializer

ZERO = 0


class TaskModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(todolist__user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if "todo_list_id" in self.request.POST:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        return Response("todo_list_id is required", status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        todo_list_id = self.request.POST["todo_list_id"]
        if serializer.is_valid():
            new_task = serializer.save()
            list_instance = ToDoList.objects.get(id=todo_list_id)
            list_instance.tasks.add(new_task)

    def destroy(self, request, *args, **kwargs):
        if "todo_list_id" in self.request.POST:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("todo_list_id is required", status=status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        todo_list_id = self.request.POST["todo_list_id"]
        current_list = get_object_or_404(ToDoList, id=todo_list_id)
        task = self.get_object()
        current_list.tasks.remove(task)
        is_task_in_no_list = task.todolist_set.count() == ZERO
        if is_task_in_no_list:
            task.delete()

    @action(detail=True, methods=["get"])
    def generate_short_link(self, request, pk=None):
        task = get_object_or_404(Task, id=pk)
        short_link, created = TaskLink.objects.get_or_create(task=task)
        return Response({"short_link": short_link.uuid})

    @action(detail=False, methods=["post"])
    def create_task_by_shorten_link(self, request):
        if "todo_list_id" in self.request.POST and "shorten_link" in self.request.POST:
            short_link = get_object_or_404(
                TaskLink, uuid=self.request.POST["shorten_link"]
            )
            new_task = short_link.task
            list_instance = ToDoList.objects.get(id=self.request.POST["todo_list_id"])
            list_instance.tasks.add(new_task)
            return Response(status=status.HTTP_201_CREATED)
        return Response("todo_list_id is required", status=status.HTTP_400_BAD_REQUEST)
