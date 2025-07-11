from django.urls import path
from . import views

app_name = 'pet_store'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('store/<int:store_id>/', views.store_detail, name='store_detail'),
    path('update/', views.update_store, name='update_store'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
]