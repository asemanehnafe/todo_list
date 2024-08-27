from celery import shared_task
from django.utils import timezone

from todo_list.models import Task


@shared_task
def my_task(arg1, arg2):
    result = arg1 + arg2
    print(result)
    return result


@shared_task
def check_deadlines():
    now = timezone.now().date()
    tasks = Task.objects.filter(deadline__lte=now)
    for task in tasks:
        task.state = True
        task.save()
