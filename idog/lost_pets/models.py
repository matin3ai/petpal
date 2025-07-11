from django.db import models
from django.conf import settings
from pet_owner.models import Pet

class LostPet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    last_seen = models.CharField(max_length=200)
    date_lost = models.DateField(null=True, blank=True, default=None)
    photo = models.ImageField(upload_to='lost_pets/', blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet.name} - {self.owner.username}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['pet'], name='unique_lost_pet'),
        ]