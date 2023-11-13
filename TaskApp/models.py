from django.db import models
from .constants import PRIORITY, STATUS

class TaskModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(choices=STATUS)
    photos = models.ImageField(upload_to='images/')
    priority = models.CharField(choices=PRIORITY)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"