from requests import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from todo_list.models import Task, TaskLink
from todo_list.serializer import TaskLinkSerializer


class GenerateShortLinkView(CreateAPIView):
    queryset = TaskLink.objects.all()
    serializer_class = TaskLinkSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {"read_only": True}

    def perform_create(self, serializer):
        task = Task.objects.get(id=self.kwargs["task_id"])
        serializer.save(task=task)
