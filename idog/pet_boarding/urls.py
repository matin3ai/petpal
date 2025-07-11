from django.urls import path
from . import views

app_name = 'pet_boarding'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('boarding/<int:boarding_id>/', views.boarding_detail, name='boarding_detail'),
    path('update/', views.update_boarding, name='update_boarding'),
]



