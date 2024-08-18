from rest_framework.generics import ListAPIView

from todo_list.models import Task
from todo_list.serializer import TaskSerializer


class TodoListDetailView(ListAPIView):
    model = Task
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all().filter(
            todolist__id=self.kwargs["todo_list_id"], todolist__user=self.request.user
        )
