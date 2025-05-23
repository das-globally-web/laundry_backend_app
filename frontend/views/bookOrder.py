import os
from django.shortcuts import render

from product.models import ProductTable

def bookOrder(request):
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
    return render(request,  'bookorder.html', { 'context': context,'product': ProductTable.objects.all().order_by('-id')})