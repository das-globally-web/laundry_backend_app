import os
import uuid
from datetime import datetime
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .model import BlogsTable
from categoryBlog.model import BlogCategory
from datetime import datetime
def add_blog_view(request):
    message = ""
    categories = BlogCategory.objects.all()
    
    if request.method == 'POST':
        categoryId = request.POST.get('categoryId')
        title = request.POST.get('title')
        content = request.POST.get('content')
        created_date = datetime.now().strftime("%B %d, %Y")
        image_file = request.FILES.get('image')

        if categoryId and title and content and created_date and image_file:
            # Image handling
            ext = image_file.name.split('.')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            file_path = os.path.join('uploads', filename)

            saved_path = default_storage.save(file_path, ContentFile(image_file.read()))
            image_url = default_storage.url(saved_path)

            BlogsTable(
                categoryId=categoryId,
                title=title,
                content=content,
                image=image_url,
                created_date=created_date
            ).save()

            message = "Blog added successfully!"

    return render(request, 'add_blog.html', {
        'message': message,
        'categories': categories,
        'today': datetime.now().strftime("%B %d, %Y")
    })
