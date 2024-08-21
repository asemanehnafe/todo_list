from rest_framework import serializers

from todo_list.models import ToDoList
from todo_list.serializer.task_serializer import TaskSerializer


class TodoListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = ToDoList
        fields = ["name", "id", "tasks"]
