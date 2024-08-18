from rest_framework.generics import DestroyAPIView

from todo_list.models import ToDoList
from todo_list.serializer import TodoListSerializer


class DeleteTodoListView(DestroyAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TodoListSerializer
