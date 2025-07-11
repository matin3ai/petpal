from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('pet-owner/', include('pet_owner.urls')),
    path('vet-clinic/', include('vet_clinic.urls')),
    path('pet-boarding/', include('pet_boarding.urls', namespace='pet_boarding')),
    path('pet-grooming/', include('pet_grooming.urls')),
    path('pet-store/', include('pet_store.urls')),
    path('lost-pets/', include('lost_pets.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



