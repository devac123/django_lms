from django.shortcuts import render,get_object_or_404,redirect, HttpResponse
from django.conf import settings
from base.forms.ContactForm import ContactUsForm
from core.usefulFunctions import UsefullFunction

def Apps(req):
    return render(req, 'admin/apps.html')
