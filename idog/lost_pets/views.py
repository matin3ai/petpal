from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import LostPet
from .forms import LostPetForm

def list_lost_pets(request):
    lost_pets = LostPet.objects.all()
    return render(request, 'lost_pets/list.html', {'lost_pets': lost_pets})

@login_required
def add_lost_pet(request):
    if request.user.role != 'owner':
        return redirect('home')
    if request.method == 'POST':
        form = LostPetForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            lost_pet = form.save(commit=False)
            lost_pet.owner = request.user
            lost_pet.save()
            return redirect('lost_pets:list')
        else:
            print(form.errors) 
    else:
        form = LostPetForm(user=request.user)
    return render(request, 'lost_pets/add.html', {'form': form})