"""
URL configuration for ironAppBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ironAppBackend import settings
from .views import file_upload
from frontend.views.homeview import home
from frontend.views.aboutview import aboutus
from frontend.views.serviceview import service
from frontend.views.priceview import price
from frontend.views.contactus import contactUs
from frontend.views.blogview import blog, blogsByCategory
from frontend.views.login import login, verify_otp, signup_view
urlpatterns = [
    # this all Website aroute inculde main website
    path('', home, name='home'),
    path("login/", login, name="login"),
    path("register/", signup_view, name="register"),
    path("verify-otp/",verify_otp, name="verify_otp"),
    path('aboutus', aboutus, name='aboutus'),
    path('service', service, name="service"),
    path("price", price, name="price"),
    path("contactus", contactUs, name="contactus"),
    path("blog", blog, name="blog"),
    path("blog/<str:id>", blogsByCategory, name="blog_by_category"),

    # before this include the upper code was for main website route

    path('api/', include('users.urls')),
    path('api/', include('banners.urls')),
    path('api/', include('service.urls')),
    path('api/', include('product.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('slots.urls')),
    path('admin/', include('myAdmin.urls')),
    path('api/upload/', file_upload, name="file_upload")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



