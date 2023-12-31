from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import TaskModel
from .constants import FILTER_CHOICES

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='First Name')
    last_name = forms.CharField(max_length=150, required=False, help_text='Last Name')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    photos = MultipleFileField()
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'due_date', 'photos', 'priority']
        
        
class MixedTaskPhotoForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    photos = MultipleFileField()
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'due_date', 'photos', 'priority', 'image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
    
    def save(self, commit=True):
        task = super().save(commit=False)
        task.image = self.cleaned_data['image']
        if commit:
            task.save()
        return task
    
    
    
class TaskSearchForm(forms.Form):
    search = forms.CharField(label='Search', required=False)
    
    
class TaskFilterForm(forms.Form):
    filter_option = forms.ChoiceField(choices=FILTER_CHOICES, required=False)