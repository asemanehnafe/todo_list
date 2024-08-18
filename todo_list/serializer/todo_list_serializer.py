from rest_framework import serializers

from todo_list.models import ToDoList


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ["name", "id"]
