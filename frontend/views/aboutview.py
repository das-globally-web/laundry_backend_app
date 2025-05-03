import os
from product.models import ProductTable
from django.shortcuts import render


def aboutus(request):

    return render(request, 'aboutus.html' )