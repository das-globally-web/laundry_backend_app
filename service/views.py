from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from service.models import ServiceTable
from .serializers import ServiceSerializer

@csrf_exempt
def service_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = ServiceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "User registered successfully"}, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def get_all_service(request):
    if request.method == 'GET':
        users = ServiceTable.objects.all()
        tojson = users.to_json()
        fromjson = json.loads(tojson)
      
        return JsonResponse({"message": "All service", "data": fromjson}, safe=False, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def get_populer_service(request):
    if request.method == 'GET':
        populer_service = []
        users = ServiceTable.objects.all()
        for service in users:
            if service.rating > 4:
                populer_service.append(json.loads(service.to_json()))
        
      
        return JsonResponse({"message": "All service", "data": populer_service}, safe=False, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)