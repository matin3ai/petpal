from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Grooming
from .forms import GroomingForm

@login_required
def dashboard(request):
    if request.user.role != 'grooming':
        return redirect('home')
    grooming, created = Grooming.objects.get_or_create(user=request.user)
    return render(request, 'pet_grooming/dashboard.html', {'grooming': grooming})

def grooming_detail(request, grooming_id):
    grooming = get_object_or_404(Grooming, id=grooming_id)
    return render(request, 'pet_grooming/grooming_detail.html', {'grooming': grooming})

@login_required
def update_grooming(request):
    if request.user.role != 'grooming':
        return redirect('home')
    grooming, created = Grooming.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = GroomingForm(request.POST, request.FILES, instance=grooming)
        if form.is_valid():
            form.save()
            return redirect('pet_grooming:dashboard')
    else:
        form = GroomingForm(instance=grooming)
    return render(request, 'pet_grooming/grooming_form.html', {'form': form})