import os
from django.shortcuts import render
from categoryBlog.model import BlogCategory
from blog.model import BlogsTable
def blog(request):
    category = BlogCategory.objects.all().order_by('-id')
    
    query = request.GET.get('q')  # Get search keyword from form input
    if query:
        blog = BlogsTable.objects.filter(title__icontains=query).order_by('-id')  # Search by title
    else:
        blog = BlogsTable.objects.all().order_by('-id')
    
    return render(request, 'blog.html', {'category': category, 'blogs': blog})

def blogsByCategory(request, id):
    category = BlogCategory.objects.all().order_by('-id')
    query = request.GET.get('q')

    if query:
        blog = BlogsTable.objects.filter(categoryId=id, title__icontains=query).order_by('-id')
    else:
        blog = BlogsTable.objects.filter(categoryId=id).order_by('-id')

    return render(request, 'blog.html', {'category': category, 'blogs': blog})
