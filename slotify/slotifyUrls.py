from django.urls import path
from slotify.views import SlotifyDashboard
from slotify.views import SlotifyServiceList
from slotify.views import SlotifyServiceDetail


urlpatterns =[
    path('slotify/',SlotifyDashboard.SlotifyDashboard, name='SlotifyDashboard'),
    path('services/',SlotifyServiceList.SlotifyServiceList, name='SlotifyServiceList'),
    path('service_detail/<int:id>',SlotifyServiceDetail.SlotifyServiceDetail, name='service_details')
]