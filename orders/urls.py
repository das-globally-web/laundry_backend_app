from django.urls import path, include
from .views import create_order, get_order_perticuler, get_orders, update_status, update_quantity, get_orders_userid


urlpatterns = [
    path('create-order', create_order, name="create_banner"),
    path('get-orders', get_orders, name="banners_get"),
    path('update-status-orders', update_status, name="update_status"),
    path('update-quantity-orders', update_quantity, name="update_quantity"),
    path('orders-users/<str:id>',get_orders_userid, name="get_orders_userid"),
    path('perticuler-order/<str:id>',get_order_perticuler, name="get_order_perticuler"),

]