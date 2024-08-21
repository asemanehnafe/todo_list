from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from todo_list.models import ToDoList
from todo_list.serializer import TodoListSerializer


class TasKModelViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ToDoList.objects.filter(user=request.user)
        serializer = TodoListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ToDoList.objects.all()
        todo_list = get_object_or_404(queryset, pk=pk)
        serializer = TodoListSerializer(todo_list)
        return Response(serializer.data)

    def create(self, request):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def udate(self, request, pk=None):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        queryset = ToDoList.objects.all()
        todo_list = get_object_or_404(queryset, pk=pk)
        todo_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
