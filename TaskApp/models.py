from django.db import models
from django.contrib.auth.models import User
from .constants import PRIORITY

class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(choices=PRIORITY)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return f"{self.title}"
    
    
class PhotoModel(models.Model):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE, related_name='tasks')
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return f"{self.task.title}"

