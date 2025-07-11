from django.contrib import admin
from .models import Boarding

@admin.register(Boarding)
class BoardingAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'capacity', 'supported_animals']
    list_filter = ['supported_animals']
    search_fields = ['name', 'address']