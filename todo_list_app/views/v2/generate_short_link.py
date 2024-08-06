from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from todo_list_app.models import Task, TaskLink


class GenerateShortLink(TemplateView, LoginRequiredMixin):

    template_name = 'todo_list_app/v1/generate_short_link.html'

    def get_context_data(self, **kwargs):
        task_id = self.kwargs['task_id']
        task = get_object_or_404(Task, id=task_id)
        short_link, created = TaskLink.objects.get_or_create(task=task)
        context = super().get_context_data(**kwargs)
        context['short_link'] = short_link
        return context