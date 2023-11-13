from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskListView.as_view(), name='homepage'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('show_tasks/', TaskListView.as_view(), name='show_tasks'),
    path('login/', LogInView.as_view(), name='loginpage'),
]
