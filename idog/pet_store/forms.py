from django import forms
from .models import Store, Product

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address', 'contact_info', 'photo', 'supported_animals']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'supported_animals', 'price', 'photo']