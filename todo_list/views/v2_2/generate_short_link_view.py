from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views import View

from todo_list.models import Task, TaskLink


@method_decorator(login_required, name="dispatch")
class GenerateShortLinkView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        short_link, created = TaskLink.objects.get_or_create(task=task)
        return render(
            request,
            "todo_list_app/v1/generate_short_link.html",
            {"short_link": short_link},
        )
