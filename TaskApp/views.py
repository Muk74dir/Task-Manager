from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm, TaskForm
from .models import TaskModel


class BaseLoginRequiredMixin(LoginRequiredMixin, View):
    login_url = 'loginpage'
    
# LogIn View
class LogInView(LoginView):
    template_name = 'login.html'
    
    def post(self, rquest):
        username = rquest.POST['username']
        password = rquest.POST['password']
        user = authenticate(rquest, username=username, password=password)
        if user is not None:
            login(rquest, user)
            return redirect('show_tasks')
        else:
            return render(rquest, self.template_name, {'Error': 'Invalid Username or Password'})
     
# TaskList View
class TaskListView(BaseLoginRequiredMixin):
    template_name = 'show_tasks.html'
    success_url = '/show_tasks/'

    def get(self, request):
        tasks = TaskModel.objects.filter(user=request.user)
        context = {'tasks':tasks}    
        return render(request, self.template_name, context)      
        
# Add Task View
class AddTaskView(BaseLoginRequiredMixin, CreateView):
    model = TaskModel
    form_class = TaskForm
    template_name = 'add_task.html'
    success_url = '/show_tasks/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'signup.html'
    success_url = '/login/'
    
    
# Logout View
class LogOutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('loginpage')
    
            


