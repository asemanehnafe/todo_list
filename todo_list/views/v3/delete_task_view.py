from rest_framework import status
from rest_framework.generics import DestroyAPIView, get_object_or_404
from rest_framework.response import Response

from todo_list.models import Task, ToDoList
from todo_list.serializer import TaskSerializer

ZERO = 0


class DeleteTaskView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def delete(self, request, *args, **kwargs):
        todo_list_id = self.kwargs["todo_list_id"]
        current_list = get_object_or_404(ToDoList, id=todo_list_id)
        task = self.get_object()
        current_list.tasks.remove(task)
        is_task_in_no_list = task.todolist_set.count() == ZERO
        if is_task_in_no_list:
            task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
