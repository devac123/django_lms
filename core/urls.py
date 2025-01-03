from django.contrib import admin
from django.urls import path,include
from . import views, settings
from django.conf.urls.static import static
from base.views import HomePageView
from base.views import AppsPageView

admin.site.site_title = settings.SITE_TITLE
admin.site.site_header = settings.SITE_HEADER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',HomePageView.home,name="home"),
    path('', include('todo_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('apps/', AppsPageView.Apps, name="app"),
    path('accounts/logout', views.logout_page, name='logout'), 
    path('profile/', views.profile_view, name='profile'),
    path('password-reset/', views.change_password, name='change_password'),
    path('password-reset/<uidb64>/<token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
    path('create_account/', views.create_account, name='create_account'),
    path('chat/', include('chat.chaturls')),  # Routes to the chat app
    path('services/', include('basic_services.urls')),  # Routes to the chat app
    
]

# slotify booking routs
urlpatterns += [
    path('apps/', include('slotify.slotifyUrls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)