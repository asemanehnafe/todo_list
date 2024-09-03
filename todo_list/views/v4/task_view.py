from django.shortcuts import get_object_or_404
from rest_framework import exceptions, status, viewsets
from rest_framework.response import Response

from todo_list.models import Task
from todo_list.serializer import TaskSerializer


class TasKModelViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return Task.objects.filter(todolist__user=self.request.user)

    def list(self, request):
        todo_list_id = self.request.POST["todo_list_id"]
        tasks = self.get_queryset().filter(todo_list_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todo_list = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = TaskSerializer(todo_list)
        return Response(serializer.data)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def udate(self, request, pk=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        todo_list = get_object_or_404(self.get_queryset(), pk=pk)
        todo_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
