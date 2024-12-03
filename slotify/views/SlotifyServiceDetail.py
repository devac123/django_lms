from django.shortcuts import render, get_object_or_404
from slotify.slotifyModels.SlotifyServices import SlotifyService
from slotify.slotifyModels.SlotifyServiceSlot import SlotifyServiceSlot

def SlotifyServiceDetail(req,id):
    service = get_object_or_404(SlotifyService, id=id)
    content={
        'data' : {
            'id': id,
            'service' : service
        }
    }
    return render(req,'slotify/SlotifyServiceDetail.html',content)