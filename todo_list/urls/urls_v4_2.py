from django.urls import path
from rest_framework.routers import DefaultRouter

from todo_list.views.v4_2 import *

router = DefaultRouter()
router.register(r"todo_lists", TodoListModelViewSet, basename="todo_list")
router.register(r"tasks", TaskModelViewSet, basename="task")

# urlpatterns = [path("", TaskModelViewSet.as_view(), name="all_todo_lists_view_v3")]
urlpatterns = router.urls
