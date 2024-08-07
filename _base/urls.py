"""
URL configuration for _base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo_list.views.main_page import main_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('v1/', include('todo_list.urls.urls_v1')),
    path('v2_2/', include('todo_list.urls.urls_v2_2')),
    path('v2/', include('todo_list.urls.urls_v2')),
]
