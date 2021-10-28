from django.urls import path

from todo_list.base.models import Task
from .views import TaskList 

urlpatterns= [
    path('',TaskList.as_view(),name='tasks'),
]