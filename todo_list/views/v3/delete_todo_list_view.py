from rest_framework.generics import DestroyAPIView, get_object_or_404

from todo_list.models import ToDoList
from todo_list.serializer import TodoListSerializer

ONE = 1


class DeleteTodoListView(DestroyAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = TodoListSerializer

    def delete(self, request, *args, **kwargs):
        deleting_todo_list = get_object_or_404(ToDoList, pk=self.kwargs["pk"])
        for task in deleting_todo_list.tasks.all():
            is_task_only_in_this_list = task.todolist_set.count() == ONE
            if is_task_only_in_this_list:
                task.delete()
        return super().delete(self, request, *args, **kwargs)
