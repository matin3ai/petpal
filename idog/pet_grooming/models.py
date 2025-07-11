from django.db import models
from django.conf import settings

class Grooming(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='groomings/', blank=True)
    services = models.TextField()
    supported_animals = models.CharField(max_length=200)
    pricing = models.TextField(blank=True)
    working_hours = models.CharField(max_length=200, blank=True)  

    def __str__(self):
        return self.name