from django.shortcuts import render, get_object_or_404
from slotify.slotifyModels.SlotifyServices import SlotifyService
from slotify.slotifyModels.SlotifyServiceSlot import SlotifyServiceSlot
import json

def SlotifyServiceDetail(req, id):
    service = get_object_or_404(SlotifyService, id=id)
    slots = SlotifyServiceSlot.objects.filter(service_id=id)
    slot_data = [
        {
            'start': slot.start_time.isoformat(),
            'end': slot.end_time.isoformat(),
            'title': f"Available" if slot.is_available else "Not Available",
            'color': "green" if slot.is_available else "red",
        }
        for slot in slots
    ]

    context = {
        'data' : {
            'id' : id,
            'serviceDetail' : service,
            'slots' :   json.dumps(slot_data)
        }
    }
    return render(req,'slotify/SlotifyServiceDetail.html',context)