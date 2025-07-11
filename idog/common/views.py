from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

@login_required
def add_review(request):
    if request.user.role != 'owner':
        return redirect('home')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'common/review_form.html', {'form': form})