from django.contrib import admin
from .models import Clients
# Register your models here.
admin.site.register(Clients)
class CoordinatorAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email']
    ordering = ['created_at']
    list_display = ['first_name', 'last_name', 'email', 'phone', 'active', 'created_at']
    list_filter = ['created_at'] 