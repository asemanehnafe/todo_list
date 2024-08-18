from requests import Response
from rest_framework.generics import RetrieveAPIView

from todo_list.models import Task
from todo_list.serializer import TaskSerializer


class TaskDetailView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
