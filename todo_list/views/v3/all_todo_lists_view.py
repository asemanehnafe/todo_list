from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from todo_list.models import ToDoList
from todo_list.serializer import TodoListSerializer


class AllTodoListsView(ListAPIView):
    model = ToDoList
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDoList.objects.filter(user=self.request.user)
