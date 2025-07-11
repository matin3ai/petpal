from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin' or not request.user.is_superuser:
        return redirect('home')
    return redirect('admin:index') 