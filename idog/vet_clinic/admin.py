from django.contrib import admin
from .models import VetClinic, Appointment

@admin.register(VetClinic)
class VetClinicAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'license_number', 'contact_info']
    list_filter = ['supported_animals']
    search_fields = ['name', 'address']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['vet_clinic', 'pet', 'date', 'status']
    list_filter = ['status']
    search_fields = ['vet_clinic__name', 'pet__name']