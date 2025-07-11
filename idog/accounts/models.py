from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'admin'), 
        ('owner', 'owner'),
        ('vet', 'vet'),
        ('boarding', 'boarding'),
        ('grooming', 'grooming'),
        ('store', 'store'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


    def __str__(self):
        return self.username
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Profile for {self.user.username}"