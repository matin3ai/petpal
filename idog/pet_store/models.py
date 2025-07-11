from django.db import models
from django.conf import settings

class Store(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    contact_info = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='stores/', blank=True)
    supported_animals = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supported_animals = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.name