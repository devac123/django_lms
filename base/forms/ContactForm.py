# forms.py
from django import forms
from models.Contact import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['subject', 'name', 'email', 'message']