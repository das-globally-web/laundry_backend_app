import os
from django.shortcuts import render

from product.models import ProductTable

def price(request):
    phone = request.session.get('phone', None)
    name = request.session.get('name', None)
    address = request.session.get('address', None)
    is_login = request.session.get('isLogin', False)
    userid = request.session.get('id', None)

    context = {
        'id': userid,
        'phone': phone,
        'name': name,
        'address': address,
        'is_login': is_login
    }
    product= ProductTable.objects.all().order_by('-id')
    half = len(product) // 2
    left_column = product[:half]
    right_column = product[half:]
    return render(request, 'price.html',  { 'context': context, 'products': product, "left_column": left_column,
        "right_column": right_column, 'product': ProductTable.objects.all()})