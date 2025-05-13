import os
from django.shortcuts import render

from product.models import ProductTable

def service(request):
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
    product= ProductTable.objects.all()
    return render(request,  'servicees.html', { 'context': context, 'product': ProductTable.objects.all().order_by('-id'), 'products': product})