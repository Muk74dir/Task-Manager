from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm, TaskForm

# Login View
class LogInView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage')
            else:
                return render(request, 'login.html')
        else:
            redirect (request, 'login.html')

# Registration View
class RegistrationView(View):
    def get(self, request):
        return render(request, 'registration.html')
    
    def post(self, request):
        if request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                return render(request, 'registration.html')
        else:
            form = RegistrationForm()
            return redirect('registration')    
        
# Task List View
class TaskListView(View): 
    def get(self, request):
        return render(request, 'show_tasks.html')      
        
            
# Logout View
class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

