from django.urls import path
from slotify.views import SlotifyDashboard
from slotify.views import SlotifyServiceList
from slotify.views import SlotifyServiceDetail
from slotify.Api.SlotListViewApi import SlotListView
from slotify.Api.SlotListViewApi import SlotListView
from slotify.views import SlotifyBookingCheckout

urlpatterns =[
    path('slotify/',SlotifyDashboard.SlotifyDashboard, name='SlotifyDashboard'),
    path('services/',SlotifyServiceList.SlotifyServiceList, name='SlotifyServiceList'),
    path('service_detail/<int:id>',SlotifyServiceDetail.SlotifyServiceDetail, name='service_details'),
    path('slots/<int:id>/', SlotListView.as_view(), name='slot-list'),
    path('book/<int:service_id>/slot/<int:slot_id>/', SlotifyBookingCheckout.SlotifyBookingCheckout, name='slot_detail'),
]