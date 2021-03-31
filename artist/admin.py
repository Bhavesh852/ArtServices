from django.contrib import admin
from .models import Services, Art, Booking, Contact

# Register your models here.

class Admin_Booking(admin.ModelAdmin):
	list_display = ['booking_user', 'booking_service', 'booking_phone', 'booking_date_of_service']

admin.site.register(Services)
admin.site.register(Art)
admin.site.register(Booking, Admin_Booking)
admin.site.register(Contact)