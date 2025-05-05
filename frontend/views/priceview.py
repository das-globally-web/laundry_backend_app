import os
from django.shortcuts import render

from product.models import ProductTable

def price(request):
    product= ProductTable.objects.all().order_by('-id')
    half = len(product) // 2
    left_column = product[:half]
    right_column = product[half:]
    return render(request, 'price.html',  {'products': product, "left_column": left_column,
        "right_column": right_column})