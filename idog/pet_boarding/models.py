from django.db import models
from django.conf import settings

class Boarding(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='boardings/', blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    costs = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supported_animals = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField(default=10)
    working_hours = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name