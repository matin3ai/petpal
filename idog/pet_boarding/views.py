from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Boarding
from .forms import BoardingForm

@login_required
def dashboard(request):
    if request.user.role != 'boarding':
        return redirect('home')
    boarding, created = Boarding.objects.get_or_create(user=request.user)
    return render(request, 'pet_boarding/dashboard.html', {'boarding': boarding})

def boarding_detail(request, boarding_id):
    boarding = get_object_or_404(Boarding, id=boarding_id)
    return render(request, 'pet_boarding/boarding_detail.html', {'boarding': boarding})

@login_required
def update_boarding(request):
    if request.user.role != 'boarding':
        return redirect('home')
    boarding, created = Boarding.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = BoardingForm(request.POST, request.FILES, instance=boarding)
        if form.is_valid():
            form.save()
            return redirect('pet_boarding:dashboard')
    else:
        form = BoardingForm(instance=boarding)
    return render(request, 'pet_boarding/boarding_form.html', {'form': form})


