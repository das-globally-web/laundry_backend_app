import os
from product.models import ProductTable
from django.shortcuts import render


def home(request):
    product= ProductTable.objects.all().order_by('-id')
    return render(request, 'home.html' , {'products': product})