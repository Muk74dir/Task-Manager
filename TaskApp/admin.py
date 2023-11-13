from django.contrib import admin
from .models import TaskModel

@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'status', 'photos', 'priority', 'created_at', 'updated_at']
    ordering = ['-priority']
    
    def __str__(self):
        return f"{self.title}"