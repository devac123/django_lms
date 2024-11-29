# forms.py
from django import forms
from base.models.Contact import Contact

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'name', 'email', 'message']