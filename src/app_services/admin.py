from django.contrib import admin
from .models import Service
# Register your models here.
admin.site.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['created_at']
    list_display = ['name', 'description', 'price', 'created_at']
    list_filter = ['created_at']