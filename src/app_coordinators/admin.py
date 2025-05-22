from django.contrib import admin
from .models import Coordinator


@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 'first_name', 'file_number', 'document_number',
        'email', 'phone', 'is_active', 'discharge_date'
    )
    list_filter = ('is_active', 'discharge_date')
    search_fields = ('first_name', 'last_name', 'email', 'document_number', 'file_number')
    ordering = ('last_name', 'first_name')
