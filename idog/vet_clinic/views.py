from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import VetClinic, Appointment
from .forms import VetClinicForm, AppointmentForm
from pet_owner.models import Pet

@login_required
def dashboard(request):
    if request.user.role != 'vet':
        return redirect('home')
    clinic, created = VetClinic.objects.get_or_create(user=request.user)
    appointments = Appointment.objects.filter(vet_clinic=clinic)
    return render(request, 'vet_clinic/dashboard.html', {'clinic': clinic, 'appointments': appointments})

def clinic_detail(request, clinic_id):
    clinic = get_object_or_404(VetClinic, id=clinic_id)
    return render(request, 'vet_clinic/clinic_detail.html', {'clinic': clinic})

@login_required
def update_clinic(request):
    if request.user.role != 'vet':
        return redirect('home')
    clinic, created = VetClinic.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = VetClinicForm(request.POST, request.FILES, instance=clinic)
        if form.is_valid():
            form.save()
            return redirect('vet_clinic:dashboard')
        else:
            print(form.errors) 
    else:
        form = VetClinicForm(instance=clinic)
    return render(request, 'vet_clinic/clinic_form.html', {'form': form})

@login_required
def book_appointment(request):
    if request.user.role != 'owner':
        return redirect('home')
    if request.method == 'POST':
        form = AppointmentForm(request.POST, user=request.user)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return redirect('pet_owner:dashboard')
        else:
            print(form.errors) 
    else:
        form = AppointmentForm(user=request.user)
    return render(request, 'vet_clinic/appointment_form.html', {'form': form})

@login_required
def confirm_appointment(request, appointment_id):
    if request.user.role != 'vet':
        return redirect('home')
    appointment = get_object_or_404(Appointment, id=appointment_id, vet_clinic__user=request.user)
    appointment.status = 'confirmed'
    appointment.save()
    return redirect('vet_clinic:dashboard')

@login_required
def cancel_appointment(request, appointment_id):
    if request.user.role != 'vet':
        return redirect('home')
    appointment = get_object_or_404(Appointment, id=appointment_id, vet_clinic__user=request.user)
    appointment.status = 'cancelled'
    appointment.save()
    return redirect('vet_clinic:dashboard')