from django.shortcuts import render
from django.views import View


# Hompepage View
class HomeView(View):
    def get(self, request):
        return render(request, 'base.html')
    

# Login View
class LogInView(View):
    def get(self, request):
        return render(request, 'login.html')

