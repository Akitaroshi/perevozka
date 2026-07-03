from django.contrib import admin
from .models import BookingRequest

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'phone', 'service_type', 'booking_date', 'status')
    list_filter = ('status', 'service_type')
    search_fields = ('client_name', 'phone')