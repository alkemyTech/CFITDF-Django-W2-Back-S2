from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'file_number', 'is_active', 'email', 'phone')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name', 'file_number', 'email')
    ordering = ('last_name', 'first_name')