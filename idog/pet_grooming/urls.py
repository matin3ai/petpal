from django.urls import path
from . import views

app_name = 'pet_grooming'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('grooming/<int:grooming_id>/', views.grooming_detail, name='grooming_detail'),
    path('update/', views.update_grooming, name='update_grooming'),
]