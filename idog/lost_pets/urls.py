from django.urls import path
from . import views

app_name = 'lost_pets'
urlpatterns = [
    path('', views.list_lost_pets, name='list'),
    path('add/', views.add_lost_pet, name='add'),
]