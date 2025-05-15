from django.contrib import admin
from .models import Coordinator


@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    search_fields = ['document_number']
