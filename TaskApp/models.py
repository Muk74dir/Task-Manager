from django.db import models
from django.contrib.auth.models import User
from .constants import PRIORITY

class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    photos = models.ImageField(upload_to='images/')
    priority = models.CharField(choices=PRIORITY)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"