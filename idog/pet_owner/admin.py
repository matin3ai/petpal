from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'species', 'breed', 'qr_code_active']
    list_filter = ['species', 'qr_code_active']
    search_fields = ['name', 'owner__username']