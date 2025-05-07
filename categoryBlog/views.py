from django.shortcuts import render
from .model import BlogCategory
def add_category_view(request):
    message = ""
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            BlogCategory(title=title).save()
            message = "Category added successfully!"
    return render(request, 'add_category.html', {'message': message})
