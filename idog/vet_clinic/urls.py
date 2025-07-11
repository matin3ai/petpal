from django.urls import path
from . import views

app_name = 'vet_clinic'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clinic/<int:clinic_id>/', views.clinic_detail, name='clinic_detail'),
    path('update/', views.update_clinic, name='update_clinic'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('confirm-appointment/<int:appointment_id>/', views.confirm_appointment, name='confirm_appointment'),
    path('cancel-appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
]