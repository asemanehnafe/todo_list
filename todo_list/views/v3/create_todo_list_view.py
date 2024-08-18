from rest_framework.generics import CreateAPIView

from todo_list.models import ToDoList
from todo_list.serializer import TodoListSerializer


class CreateTodoListView(CreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TodoListSerializer
