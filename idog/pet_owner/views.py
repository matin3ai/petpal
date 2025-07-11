from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pet
from .forms import PetForm
from vet_clinic.models import Appointment
import qrcode
from io import BytesIO
from django.conf import settings
import os

@login_required
def dashboard(request):
    if request.user.role != 'owner':
        return redirect('home')
    pets = Pet.objects.filter(owner=request.user)
    appointments = Appointment.objects.filter(pet__owner=request.user)
    return render(request, 'pet_owner/dashboard.html', {'pets': pets, 'appointments': appointments})



@login_required
def add_pet(request):
    if request.user.role != 'owner':
        return redirect('home')
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('pet_owner:dashboard')
        else:
            print(form.errors)
    else:
        form = PetForm()
    return render(request, 'pet_owner/pet_form.html', {'form': form})

@login_required
def edit_pet(request, pet_id):
    if request.user.role != 'owner':
        return redirect('home')
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_owner:dashboard')
    else:
        form = PetForm(instance=pet)
    return render(request, 'pet_owner/pet_form.html', {'form': form})


@login_required
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'pet_owner/pet_detail.html', {'pet': pet})

@login_required
def view_qr_code(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    owner_profile = pet.owner.userprofile if hasattr(pet.owner, 'userprofile') else None
    if request.GET.get('format') == 'image':
        pet_url = request.build_absolute_uri(f"/pet-owner/qr-code/{pet.id}/")
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(pet_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        return HttpResponse(buffer, content_type="image/png")
    return render(request, 'pet_owner/owner_info.html', {'pet': pet, 'owner': pet.owner, 'owner_profile': owner_profile})