from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'active', 'created_at', 'updated_at')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)