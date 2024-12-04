from django.contrib import admin
from .slotifyModels.SlotifyServices import SlotifyService
from .slotifyModels.SlotifyUserBooking import SlotifyBooking
from .slotifyModels.SlotifyServiceSlot import SlotifyServiceSlot
from .slotifyModels.SlotifyUserData import SlotifyUserData

class SlotifyUserDataAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'user_id' ,'phone_number', 'address', 'birth_date')  # Fields to show in list view
    search_fields = ['user__username', 'phone_number']  # Fields that can be searched
    list_filter = ('birth_date',)  # Add filtering based on birth_date
    ordering = ['user__username']  # Default ordering

class SlotifyServiceSlotAdmin(admin.ModelAdmin):
    # List display
    list_display = ('service', 'start_time', 'end_time', 'is_available')
    list_filter = ('service', 'is_available', 'start_time')  # Filters in the sidebar
    search_fields = ('service__name',)  # Assuming SlotifyService has a 'name' field
    ordering = ('start_time',)  # Default ordering

admin.site.register(SlotifyUserData,SlotifyUserDataAdmin)
admin.site.register(SlotifyBooking)
admin.site.register(SlotifyService)
admin.site.register(SlotifyServiceSlot,SlotifyServiceSlotAdmin)
# Register your models here.
