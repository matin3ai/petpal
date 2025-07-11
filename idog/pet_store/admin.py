from django.contrib import admin
from .models import Store, Product

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'contact_info']
    search_fields = ['name', 'address']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'store', 'category', 'price']
    list_filter = ['category', 'supported_animals']
    search_fields = ['name', 'store__name']