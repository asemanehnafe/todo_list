from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_base.settings")

app = Celery("todo_list", broker="redis://localhost:6379")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks(["todo_list.tasks"])

app.conf.beat_schedule = {
    "add-every-day": {
        "task": "todo_list.tasks.expire_tasks.check_deadlines",
        "schedule": 24 * 3600.0,
        "args": (),
    },
}
app.conf.timezone = "UTC"
