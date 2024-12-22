from django.shortcuts import render,get_object_or_404,redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from .forms import SignupForm
from base.forms.ContactForm import ContactUsForm
from . import usefulFunctions

# Create your views here.

@login_required
def profile_view(request):
    context = {
        'user': request.user,
    }
    return render(request, 'user/profile.html', context)  


@login_required
def logout_page(request):
    logout(request)
    return redirect('/') 



def change_password(req):
    if req.method == 'POST':
        form = PasswordResetForm(req.POST)
        if form.is_valid():
            # Get the email from the form
            email = form.cleaned_data.get('email')
            users = User.objects.filter(email=email)
            if users.exists():
                token = None
                for user in users:
                    token = default_token_generator.make_token(user)
                    uid = urlsafe_base64_encode(str(user.pk).encode('utf-8'))

                    reset_link = req.build_absolute_uri(
                        f'/password-reset/{uid}/{token}/'
                    )

                    usefulFunctions.send_email(message=reset_link, sender=settings.EMAIL_HOST_USER, reciever=email)

                    alerts = {
                        'message' : 'Please check Your email We have shared password reset link with You'    
                    }

                if token:
                    return render(req, 'registration/change_password.html',alerts)                
    form = PasswordResetForm()
    return render(req, 'registration/change_password.html',{'form': form})


def password_reset_confirm_view(request, uidb64, token):
    try:
        # Decode the user ID from the URL
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Check if the token is valid for the user
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been reset successfully. You can now log in with your new password.")
                return redirect(reverse('login'))
        else:
            
            form = SetPasswordForm(user)
        return render(request, 'registration/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "The reset link is invalid, possibly because it has already been used.")
        return redirect('password_reset')
    



def create_account(req):
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)  # Log the user in after signup (optional)
            messages.success(req, "Signup successful. You are now logged in.")
            return redirect('/')  # Redirect to a home page or another view
        else:
            messages.error(req, "There was an error with your signup.")
    else:
        form = SignupForm()
    
    return render(req, 'registration/create_account.html',{'form': form})