from django.db import models
from django.conf import settings
from pet_owner.models import Pet

class VetClinic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='vet_clinics/', blank=True)
    services = models.TextField()
    supported_animals = models.CharField(max_length=200)
    license_number = models.CharField(max_length=100)
    working_hours = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    vet_clinic = models.ForeignKey(VetClinic, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'pending'),
        ('confirmed', 'confirmed'),
        ('cancelled', 'cancelled')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.pet.name} at {self.vet_clinic.name} on {self.date}"