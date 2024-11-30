from django.db import models

class SlotifyService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    

    def __str__(self):
        return self.name