from django.db import models
from django.conf import settings
import qrcode
from io import BytesIO
from django.core.files import File

class Pet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.FloatField()
    birth_date = models.DateField()
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    appearance = models.TextField()
    photo = models.ImageField(upload_to='pets/', blank=True)
    medical_history = models.TextField(blank=True)
    qr_code_active = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.qr_code_active and not self.qr_code:
            qr = qrcode.QRCode()
            qr.add_data(f'Owner: {self.owner.username}, Contact: {self.owner.email}, Pet: {self.name}')
            qr.make()
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer)
            filename = f'qr_{self.owner.username}_{self.id}.png'
            self.qr_code.save(filename, File(buffer), save=False)
            super().save(*args, **kwargs)


