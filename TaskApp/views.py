from django.shortcuts import render, redirect
from django.views.generic import CreateView, View, FormView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm, TaskForm, MixedTaskPhotoForm
from .models import TaskModel, PhotoModel


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
class TaskListView(BaseLoginRequiredMixin, View):
    template_name = 'show_tasks.html'
    success_url = '/show_tasks/'

    def get(self, request):
        context = {}
        tasks = TaskModel.objects.filter(user=request.user)
        context['tasks'] = tasks
        return render(request, self.template_name, context)      
        
# Add Task View
class AddTaskView(BaseLoginRequiredMixin, CreateView):
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = '/show_tasks/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        fils = self.request.FILES.getlist('photos')
        tasks = form.save()
        for f in fils:
            PhotoModel.objects.create(task=tasks, image=f)
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
    
# Edit Task View
class EditTaskView(BaseLoginRequiredMixin, CreateView):
    template_name = 'edit_task.html'
    
    def get(self, request, id):
        task = TaskModel.objects.get(id=id)
        form = MixedTaskPhotoForm(instance=task)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, id):
        task = TaskModel.objects.get(id=id)
        form = MixedTaskPhotoForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
        else:
            return render(request, self.template_name, {'form':form})
        
    
    
    

# Complete Task View
class CompleteTaskView(BaseLoginRequiredMixin, View):
    def get(self, request, id):
        task = TaskModel.objects.get(id=id)
        task.is_completed = True
        task.save()
        return redirect('show_tasks') 

# InComplete Task View
class InCompleteTaskView(BaseLoginRequiredMixin, View):
    def get(self, request, id):
        task = TaskModel.objects.get(id=id)
        task.is_completed = False
        task.save()
        return redirect('show_tasks')
        
        
# Delete Task View
class DeleteTaskView(BaseLoginRequiredMixin, View):
    def get(self, request, id):
        task = TaskModel.objects.get(id=id)
        task.delete()
        return redirect('show_tasks')
    
# Details View
class DetailsView(BaseLoginRequiredMixin, View):
    template_name = 'details_view.html'
    
    def get(self, request, id):
        task = TaskModel.objects.get(id=id)
        return render(request, self.template_name, {'task':task})    
    

# Profile View
class ProfileView(BaseLoginRequiredMixin, View):
    template_name = 'profile.html'
    def get(self, request):
        context = {}
        context['user'] = request.user
        context['email'] = request.user.email
        context['first_name'] = request.user.first_name
        context['last_name'] = request.user.last_name
        return render(request, self.template_name, context)
    
# Change Password View
class ChangePasswordView(BaseLoginRequiredMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_url = '/profile/'
            



