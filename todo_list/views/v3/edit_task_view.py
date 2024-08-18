from rest_framework.generics import UpdateAPIView

from todo_list.models import Task
from todo_list.serializer import TaskSerializer


class EditTaskView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
