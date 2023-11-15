from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskListView.as_view(), name='homepage'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('show_tasks/', TaskListView.as_view(), name='show_tasks'),
    path('login/', LogInView.as_view(), name='loginpage'),
    path('logout/', LogOutView.as_view(), name='logoutpage'),
    path('signup/', RegistrationView.as_view(), name='signuppage'),
    path('edit_task/<int:id>/', EditTaskView.as_view(), name='edit_task'),
    path('complete_task/<int:id>/', CompleteTaskView.as_view(), name='complete_task'),
    path('incomplete_task/<int:id>/', InCompleteTaskView.as_view(), name='incomplete_task'),
    path('delete_task/<int:id>/', DeleteTaskView.as_view(), name='delete_task'),
    path('details_view/<int:id>/', DetailsView.as_view(), name='details_view'),
    path('profile/', ProfileView.as_view(), name='profilepage'),
    path('change_password/', ChangePasswordView.as_view(), name='chanagepass'),
]
