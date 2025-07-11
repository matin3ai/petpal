from django.shortcuts import render
from vet_clinic.models import VetClinic
from pet_boarding.models import Boarding
from pet_grooming.models import Grooming
from pet_store.models import Store, Product

def home(request):
    vet_clinics = VetClinic.objects.all()[:3]
    boardings = Boarding.objects.all()[:3]
    groomings = Grooming.objects.all()[:3]
    stores = Store.objects.all()[:3]
    products = Product.objects.all()[:6]
    return render(request, 'core/home.html', {
        'vet_clinics': vet_clinics,
        'boardings': boardings,
        'groomings': groomings,
        'stores': stores,
        'products': products,
    })