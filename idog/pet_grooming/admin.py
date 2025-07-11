from django.contrib import admin
from .models import Grooming

@admin.register(Grooming)
class GroomingAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'services', 'supported_animals']
    list_filter = ['supported_animals']
    search_fields = ['name', 'services']