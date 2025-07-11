from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'username or password is wrong.')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    if request.user.role == 'admin':
        return redirect('admin:index')
    elif request.user.role == 'owner':
        return redirect('pet_owner:dashboard')
    elif request.user.role == 'vet':
        return redirect('vet_clinic:dashboard')
    elif request.user.role == 'boarding':
        return redirect('pet_boarding:dashboard')
    elif request.user.role == 'grooming':
        return redirect('pet_grooming:dashboard')
    elif request.user.role == 'store':
        return redirect('pet_store:dashboard')