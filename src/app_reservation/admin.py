from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'employee',
                    'coordinator', 'reservation_date', 'service_date')
    search_fields = ('client__first_name', 'client__last_name',
                     'service__name', 'employee__first_name', 'employee__last_name')
    list_filter = ('reservation_date', 'service_date', 'employee')
    ordering = ('service_date',)
