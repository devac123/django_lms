from django.db import models
from django.contrib.auth.models import User
from  .SlotifyServices import SlotifyService

class SlotifyBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed')
    ]

    PAYMENT_STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('refunded', 'Refunded')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_history')
    service = models.ForeignKey(SlotifyService, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')  # The service being booked
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='unpaid')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending') 
    booking_date = models.DateTimeField(auto_now_add=True)  # The date and time when the booking was made
    booking_time = models.DateTimeField()  # The actual time slot of the booking
     
