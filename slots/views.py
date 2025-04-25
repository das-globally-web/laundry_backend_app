from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SlotTable
from .serializers import SlotSerializer

@csrf_exempt
def create_slot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = SlotSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Slot added"}, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def get_slot(request):
    if request.method == 'GET':
        data = SlotTable.objects()
        json_data = []
        for slot in data:
            doc = slot.to_mongo().to_dict()
            doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
            json_data.append(doc)

        return JsonResponse({"data": json_data, "message": "All slots"}, safe=False, status=200)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)
