from django.urls import path
from .views.loginview import login_view, dashboard_view, logout_view
from .views.banneruploadview import uploadBanner,allBanners,delete_banner
from .views.serviceview import addService, deletService, allService
from .views.productService import addProduct, allProducts, deleteProduct
from .views.ordersviews import allOrders
from .views.slotview import create_slot, list_slots
from .views.staffview import addstaff_user, get_staff
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('uploadBanner/',uploadBanner, name="uploadBanner"),
    path('allBanners/', allBanners, name="allBanners"),
    path('delete_banner/<id>', delete_banner, name="delete_banner"),
    path('addService/', addService, name="addService"),
    path('allService/', allService, name="allService"),
    path('delete-service/<str:id>/', deletService, name='deletService'),
    path('addprodcut/', addProduct, name='addProduct'),
    path('allproducts/', allProducts, name='allproducts'),
    path('deleteProduct/<str:id>', deleteProduct, name='deleteProduct'),
    path('allOrders/', allOrders, name='allOrders'),
    path('addSlot/', create_slot, name="addSlot"),
    path('slot-list/', list_slots, name='slot-list'),
    path('addstaff_user/', addstaff_user, name='addstaff_user'),
    path('get_staff/', get_staff, name='get_staff'),
]
