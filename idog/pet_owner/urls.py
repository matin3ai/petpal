from django.urls import path
from . import views

app_name = 'pet_owner'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-pet/', views.add_pet, name='add_pet'),
    path('edit-pet/<int:pet_id>/', views.edit_pet, name='edit_pet'),
    path('pet/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('qr-code/<int:pet_id>/', views.view_qr_code, name='view_qr_code'),
]