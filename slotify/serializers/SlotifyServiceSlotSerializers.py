from rest_framework import serializers
from slotify.slotifyModels.SlotifyServiceSlot import SlotifyServiceSlot

class SlotifyServiceSlotSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name')  # To include the related service name

    class Meta:
        model = SlotifyServiceSlot
        fields = ['id', 'service_name', 'start_time', 'end_time', 'is_available']