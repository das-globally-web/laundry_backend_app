from django.urls import path, include
from .views import banners_get, create_banner

urlpatterns = [
    path('create-banner', create_banner, name="create_banner"),
    path('get-all-banners', banners_get, name="banners_get"),
]