from django.urls import path
from rest_framework.routers import DefaultRouter

from todo_list.views.v4 import *

router = DefaultRouter()
router.register(r"todo_lists", TodoListViewSet, basename="todo_list")


urlpatterns = router.urls
