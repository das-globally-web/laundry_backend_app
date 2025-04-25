from django.urls import path
from .views import create_product, get_product

urlpatterns = [
    path('create-product', create_product, name='create_product'),
    path('get-products', get_product, name='get_product'),
]