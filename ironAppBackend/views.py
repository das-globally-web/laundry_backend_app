import os
import uuid
from ironAppBackend import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def handle_uploaded_file(file):
    ext = file.name.split('.')[-1]
    new_filename = f"{uuid.uuid4()}.{ext}"
    file_path = os.path.join(settings.MEDIA_ROOT, new_filename)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return settings.MEDIA_URL + new_filename

@csrf_exempt
def file_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        file_path = handle_uploaded_file(file)
        return JsonResponse({"file_path": file_path}, status=201)
    return JsonResponse({"error": "No file uploaded"}, status=400)
