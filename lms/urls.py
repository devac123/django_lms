"""
URL configuration for lms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views, settings

admin.site.site_title = settings.SITE_TITLE
admin.site.site_header = settings.SITE_HEADER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('site/layout', views.layout),
    path('lms/',include('LearnHub.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/logout', views.logout_page, name='logout'), 
    path('profile/', views.profile_view, name='profile'),
    path('password-reset/', views.change_password, name='change_password'),
    path('password-reset/<uidb64>/<token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
    path('create_account/', views.create_account, name='create_account'),
    
]
