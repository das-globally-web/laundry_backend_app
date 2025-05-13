import os
from product.models import ProductTable
from django.shortcuts import render


def terms(request):
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
    return render(request, 'terms.html' , {'products': product,  'context': context, 'product': ProductTable.objects.all().order_by('-id')})

def shippingPolicy(request):
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
    return render(request, 'shipping-policy.html' , {'products': product,  'context': context, 'product': ProductTable.objects.all().order_by('-id')})

def cancellation(request):
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
    return render(request, 'cancellation-refund-policy.html' , {'products': product,  'context': context, 'product': ProductTable.objects.all().order_by('-id')})

def privacy(request):
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
    return render(request, 'privacy-policy.html' , {'products': product,  'context': context, 'product': ProductTable.objects.all().order_by('-id')})