from django.contrib import admin
from .models import LostPet

@admin.register(LostPet)
class LostPetAdmin(admin.ModelAdmin):
    list_display = ['get_pet_name', 'get_pet_species', 'get_pet_breed', 'last_seen', 'date_lost']
    list_filter = ['pet__species']

    def get_pet_name(self, obj):
        return obj.pet.name
    get_pet_name.short_description = 'Pet name'

    def get_pet_species(self, obj):
        return obj.pet.species
    get_pet_species.short_description = 'Species'

    def get_pet_breed(self, obj):
        return obj.pet.breed
    get_pet_breed.short_description = 'Breed'