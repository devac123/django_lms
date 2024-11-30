from django.urls import path
from slotify.views import SlotifyDashboard


urlpatterns =[
    path('',SlotifyDashboard.SlotifyDashboard, name='SlotifyDashboard')
]