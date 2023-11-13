from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, TaskForm
from .models import TaskModel

# Login View
class LogInView(LoginView):
    template_name = 'login.html'
    success_url = '/show_tasks/'

  
        
# TaskList View
class TaskListView(View): 
    def get(self, request):
        return render(request, 'show_tasks.html')      
        
# Add Task View
class AddTaskView(CreateView):
    model = TaskModel
    form_class = TaskForm
    template_name = 'add_task.html'
    success_url = '/show_tasks/'
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
            


