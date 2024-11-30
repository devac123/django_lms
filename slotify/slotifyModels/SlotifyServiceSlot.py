from django.db import models
from .SlotifyServices import SlotifyService

class SlotifyServiceSlot(models.Model):
    service = models.ForeignKey(SlotifyService, on_delete=models.CASCADE, related_name='slots')  # Reference to the service this slot is for
    start_time = models.DateTimeField()  # The start time of the slot
    end_time = models.DateTimeField()  # The end time of the slot
    is_available = models.BooleanField(default=True)  # Whether the slot is available for booking
    
    def __str__(self):
        return f"Slot from {self.start_time} to {self.end_time}"
    