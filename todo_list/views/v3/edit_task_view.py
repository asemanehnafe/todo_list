from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from todo_list.models import Task
from todo_list.serializer import TaskSerializer


class EditTaskView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
