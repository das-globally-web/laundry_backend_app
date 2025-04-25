import os
import uuid
from bson import ObjectId
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from banners.models import BannerTable
from banners.serializers import BannerSerializer
from .decorators import session_login_required

@session_login_required
def uploadBanner(request):
    image_url = None
    errors = None

    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        ext = uploaded_file.name.split('.')[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        file_path = os.path.join('uploads/', filename)

        # Save file to media/uploads/
        saved_path = default_storage.save(file_path, ContentFile(uploaded_file.read()))
        image_url = default_storage.url(saved_path)

        print("Uploaded image path:", image_url)

        data = {
            "image": image_url
        }

        serializer = BannerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'bannerupload.html', {
                'image_url': image_url
            })
        else:
            errors = serializer.errors  # Capture errors to pass to template

    return render(request, 'bannerupload.html', {
        'image_url': image_url,
        'errors': errors
    })

@session_login_required
def allBanners(request):
    banners = BannerTable.objects.all().order_by('-id')
    return render(request, 'allbanners.html', {'banners': banners})

@session_login_required
def delete_banner(request, id):
    banner = BannerTable.objects.get(id=ObjectId(str(id)))
    
    # You can also remove the file from media storage here if needed
    banner.delete()
    return redirect('allBanners')

