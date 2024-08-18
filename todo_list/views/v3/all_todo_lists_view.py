from rest_framework.generics import ListAPIView

from todo_list.models import ToDoList
from todo_list.serializer import TodoListSerializer


class AllTodoListsView(ListAPIView):
    model = ToDoList
    queryset = ToDoList.objects.all()
    serializer_class = TodoListSerializer

    def get_queryset(self):
        print(self.request.user)
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
