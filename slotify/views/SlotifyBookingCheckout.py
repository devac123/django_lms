from django.shortcuts import render,HttpResponse,get_object_or_404
from slotify.slotifyModels.SlotifyServices import SlotifyService
from slotify.slotifyModels.SlotifyServiceSlot import SlotifyServiceSlot


def SlotifyBookingCheckout(req, service_id, slot_id):
    service = get_object_or_404(SlotifyService, id=service_id)
    
    # Fetch the slot object by its ID
    slot = get_object_or_404(SlotifyServiceSlot, id=slot_id, service=service)  # Ensure the slot belongs to the service
    
    # Render the slot detail template with the service and slot context
    return HttpResponse('checkout page')