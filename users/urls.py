from django.urls import path, include
from .views import get_users, login_user, signup, update_address, get_user_perticuler

urlpatterns = [
    path('signup', signup, name='signup'),
    path('users', get_users, name='get_users'),
    path('login', login_user, name='login_user'),
    path('update-address', update_address, name='update_address'),
    path('get-user-perticuler/<str:id>', get_user_perticuler, name='get_user_perticuler'),
]