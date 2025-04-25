from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from product.models import ProductTable
from .serializers import ProductSerializer

@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Product added"}, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request "}, status=405)


@csrf_exempt
def get_product(request):
    if request.method == 'GET':
        users = ProductTable.objects.all()
        tojson = users.to_json()
        fromjson = json.loads(tojson)
      
        return JsonResponse({"message": "All products", "data": fromjson}, safe=False, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)