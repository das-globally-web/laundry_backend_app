from django.urls import path
from .views import service_create, get_all_service, get_populer_service

urlpatterns = [
    path('service-create',service_create, name="service_create"),
    path('get-all-service',get_all_service, name="get_all_service"),
    path('populer-service',get_populer_service, name="get_populer_service")
]