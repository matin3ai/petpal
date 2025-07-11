from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Store, Product
from .forms import StoreForm, ProductForm

@login_required
def dashboard(request):
    if request.user.role != 'store':
        return redirect('home')
    store, created = Store.objects.get_or_create(user=request.user)
    products = Product.objects.filter(store=store)
    return render(request, 'pet_store/dashboard.html', {'store': store, 'products': products})

def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    products = Product.objects.filter(store=store)
    return render(request, 'pet_store/store_detail.html', {'store': store, 'products': products})

@login_required
def update_store(request):
    if request.user.role != 'store':
        return redirect('home')
    store, created = Store.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            form.save()
            return redirect('pet_store:dashboard')
    else:
        form = StoreForm(instance=store)
    return render(request, 'pet_store/store_form.html', {'form': form})

@login_required
def add_product(request):
    if request.user.role != 'store':
        return redirect('home')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.store = Store.objects.get(user=request.user)
            product.save()
            return redirect('pet_store:dashboard')
    else:
        form = ProductForm()
    return render(request, 'pet_store/product_form.html', {'form': form})

@login_required
def edit_product(request, product_id):
    if request.user.role != 'store':
        return redirect('home')
    product = get_object_or_404(Product, id=product_id, store__user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('pet_store:dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'pet_store/product_form.html', {'form': form, 'product': product})

@login_required
def delete_product(request, product_id):
    if request.user.role != 'store':
        return redirect('home')
    product = get_object_or_404(Product, id=product_id, store__user=request.user)
    product.delete()
    return redirect('pet_store:dashboard')