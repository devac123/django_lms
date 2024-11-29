# forms.py
from django import forms
from base.models.Contact import Contact

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'name', 'email', 'message']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your name',
                'id' : 'name-field'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your email',
                'id' : 'email-field'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your message',
                'id': 'message-field'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Subject of your message',
                'id': 'subject-field'
            }),
        }