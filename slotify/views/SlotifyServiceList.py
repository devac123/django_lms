from django.shortcuts import render
from slotify.slotifyModels.SlotifyServices import SlotifyService

def SlotifyServiceList(req):
    services = SlotifyService.objects.all().values()
    context = {
        'data' : {
            'serviceList' : services
        }
    }
    return render(req,'slotify/SlotifyServiceList.html',context)