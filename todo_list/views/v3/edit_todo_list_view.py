from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from todo_list.models import ToDoList
from todo_list.serializer import TodoListSerializer


class EditTodoListView(UpdateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]
