from requests import Response
from rest_framework.generics import CreateAPIView

from todo_list.models import Task, ToDoList
from todo_list.serializer import TaskSerializer


class CreateTaskView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        new_task = serializer.save()
        list_instance = ToDoList.objects.get(id=self.kwargs["todo_list_id"])
        list_instance.tasks.add(new_task)
