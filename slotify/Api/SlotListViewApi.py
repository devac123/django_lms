from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from slotify.slotifyModels.SlotifyServiceSlot import SlotifyServiceSlot
from slotify.serializers.SlotifyServiceSlotSerializers import SlotifyServiceSlotSerializer


class SlotListView(APIView):
    def get(self, request, id, format=None):
        # Fetch the slots for a specific service
        slots = SlotifyServiceSlot.objects.filter(service_id=id)
        
        # If no slots are found, return a 404 response
        if not slots:
            return Response({'detail': 'No slots available for this service'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the slots
        serializer = SlotifyServiceSlotSerializer(slots, many=True)
        
        # Return the serialized data as JSON
        return Response({'slots': serializer.data}, status=status.HTTP_200_OK)
