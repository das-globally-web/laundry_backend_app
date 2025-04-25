import os
import uuid
from bson import ObjectId
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from myAdmin.views.decorators import session_login_required
from service.models import ServiceTable
from service.serializers import ServiceSerializer
@session_login_required
def addService(request):
    banner_image = None
    icon_image = None
    title = None
    rating = None
    errors = None
    if request.method == 'POST' and request.FILES.get('banner_image') and request.FILES.get('icon_image') and request.POST.get('title') and request.POST.get('rating'):
        title = request.POST.get('title')
        rating = request.POST.get('rating')
        banner_image = request.FILES.get('banner_image')
        icon_image = request.FILES.get('icon_image')
        def save_image(file, folder='uploads'):
            ext = file.name.split('.')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            file_path = os.path.join(folder, filename)
            saved_path = default_storage.save(file_path, ContentFile(file.read()))
            return default_storage.url(saved_path)

        banner_url = save_image(banner_image)
        icon_url = save_image(icon_image)
        data = {
            'banner_image': banner_url,
            'icon_image': icon_url,
            'title': title,
            'rating': rating,
        }
        serilizer = ServiceSerializer(data=data)
        if serilizer.is_valid():
            serilizer.save()
            print("Banner URL:", banner_url)
            print("Icon URL:", icon_url)
            return render(request, 'addservice.html', {
            'image_url': banner_url,
            'icon_url': icon_url,
            'title': title,
            'rating': rating,
            })
        else:
            errors = serilizer.errors
    return render(request, 'addservice.html', {
        'image_url': title,
        'errors': errors
    })

@session_login_required
def allService(request):
    banners = ServiceTable.objects.all().order_by('-id')
    return render(request, 'allservice.html', {'banners': banners})
@session_login_required
def deletService(request, id):
    banner = ServiceTable.objects.get(id=ObjectId(str(id)))
    
    # You can also remove the file from media storage here if needed
    banner.delete()
    return redirect('allService')