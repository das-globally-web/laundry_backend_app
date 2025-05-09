import os
from product.models import ProductTable
from django.shortcuts import render


def home(request):
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
    return render(request, 'home.html' , {'products': product,  'context': context, 'product': ProductTable.objects.all().order_by('-id')})