from django.shortcuts import render,get_object_or_404,redirect, HttpResponse
from django.conf import settings
from base.forms.ContactForm import ContactUsForm
from core.usefulFunctions import UsefullFunction

def home(req):
    context= {
        'contactForm' : ContactUsForm
    }
    if req.method == 'POST':
        form = ContactUsForm(req.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            
            try:                
                UsefullFunction.send_email(message='Thank you for reaching out. We will contact you soon.', sender=settings.EMAIL_HOST_USER, reciever=email)
                form.save()
                # Return a success response after sending email
                return HttpResponse('OK')
            except Exception as e:
                # Handle email sending error
                return HttpResponse(f'Error sending email: {str(e)}', status=500)
            
    return render(req, 'index.html',context)


