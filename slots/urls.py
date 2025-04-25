from django.urls import path, include
from .views import get_slot, create_slot

urlpatterns = [
    path('create_slot', create_slot, name='create_slot'),
    path('get-slot', get_slot, name='get_slot')
]