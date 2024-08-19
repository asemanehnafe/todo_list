from requests import Response
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from todo_list.models import Task, TaskLink, ToDoList
from todo_list.serializer import TaskLinkSerializer


class CreateTaskByShortLinkView(CreateAPIView):
    queryset = TaskLink.objects.all()
    serializer_class = TaskLinkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        short_link = get_object_or_404(TaskLink, uuid=serializer.data["uuid"])
        new_task = short_link.task
        todo_list_instance = ToDoList.objects.get(id=self.kwargs["todo_list_id"])
        todo_list_instance.tasks.add(new_task)
