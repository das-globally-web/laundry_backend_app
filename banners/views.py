from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from banners.models import BannerTable
from .serializers import BannerSerializer

@csrf_exempt
def create_banner(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = BannerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Banner added Succes"})
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=4000)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def banners_get(request):
    if request.method == 'GET':
        users = BannerTable.objects.all()
        tojson = users.to_json()
        fromjson = json.loads(tojson)
      
        return JsonResponse({"message": "here is all Banneres", "data":fromjson}, safe=False, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)