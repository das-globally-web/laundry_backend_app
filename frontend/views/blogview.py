import os
from django.shortcuts import render
from categoryBlog.model import BlogCategory
from blog.model import BlogsTable
from product.models import ProductTable
def blog(request):
    category = BlogCategory.objects.all().order_by('-id')
    
    query = request.GET.get('q')  # Get search keyword from form input
    if query:
        blog = BlogsTable.objects.filter(title__icontains=query).order_by('-id')  # Search by title
    else:
        blog = BlogsTable.objects.all().order_by('-id')
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
    return render(request, 'blog.html',  {'category': category, 'blogs': blog,  'context': context,'product': ProductTable.objects.all().order_by('-id')})

def blogsByCategory(request, id):
    category = BlogCategory.objects.all().order_by('-id')
    query = request.GET.get('q')

    if query:
        blog = BlogsTable.objects.filter(categoryId=id, title__icontains=query).order_by('-id')
    else:
        blog = BlogsTable.objects.filter(categoryId=id).order_by('-id')
    phone = request.session.get('phone', None)
    name = request.session.get('name', None)
    address = request.session.get('address', None)
    is_login = request.session.get('isLogin', False)

    context = {
        'phone': phone,
        'name': name,
        'address': address,
        'is_login': is_login
    }
    return render(request, 'blog.html',  {'category': category, 'blogs': blog,  'context': context, 'product': ProductTable.objects.all().order_by('-id')})
