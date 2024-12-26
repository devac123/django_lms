from .models import Task
from django import forms

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Task Title',
                'id' : 'title-field'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Task Description',
                'id' : 'Description-field'
            }),
            
             'status': forms.Select(attrs={
                'class': 'form-control',
                'id': 'status-field'
            }),
        }


