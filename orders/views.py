from ironAppBackend import settings
from orders.models import OrderTable
from users.models import User
from .serializers import OrderSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product.models import ProductTable
from bson import ObjectId
import json
from datetime import datetime, timedelta
import barcode
from barcode.writer import ImageWriter
import os
import qrcode


user = User.objects.all()



@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            product = []
            rawData = json.loads(request.body)
            now = datetime.now()
            formatted_time = now.strftime("%Y-%m-%d %H:%M")
            tomorrow = now + timedelta(days=1)

            for singleProduct in rawData["product"]:
                sm = json.loads(ProductTable.objects.get(id=ObjectId(singleProduct['product_id'])).to_json())
                product.append({
                    "quantity": singleProduct['quantity'],
                    "product": sm,
                    "chosed_service": singleProduct["chosed_service"]
                })

            ordercount = len(OrderTable.objects.all())
            order_id = f"order_{ordercount+1}"

            # ✅ Generate Barcode
            barcode_filename = f"barcode_{order_id}.png"
            barcode_path = os.path.join(settings.MEDIA_ROOT, 'barcodes', barcode_filename)
            os.makedirs(os.path.dirname(barcode_path), exist_ok=True)
            EAN = barcode.get_barcode_class('code128')
            ean = EAN(order_id, writer=ImageWriter())
            ean.save(barcode_path.replace(".png", ""))  # Save without extension for python-barcode

            # ✅ Generate QR Code
            qrcode_filename = f"qrcode_{order_id}.png"
            qrcode_path = os.path.join(settings.MEDIA_ROOT, 'qrcodes', qrcode_filename)
            os.makedirs(os.path.dirname(qrcode_path), exist_ok=True)
            img = qrcode.make(order_id)
            img.save(qrcode_path)
            finduser = User.objects.get(id=ObjectId(rawData["userid"]))
            data = {
                "order_id": order_id,
                "userid": rawData["userid"],
                "create_date": formatted_time,
                "delivery_date": tomorrow.strftime("%Y-%m-%d %H:%M"),
                "trx_id": rawData["trx_id"],
                "payment_tpe": rawData["payment_typ"],
                "product": product,
                "total_booked_amount": rawData["total_booked_amount"],
                "iroing": False,
                "deliverd": False,
                "barcode_path": f"/media/barcodes/{barcode_filename}",
                "qrcode_path": f"/media/qrcodes/{qrcode_filename}",
                "address": rawData["address"],
                "latitude": rawData["latitude"],
                "longitude": rawData["longitude"],
                "user": {
                    "name": finduser.name,
                    "phone": finduser.phone_number,
                },
                "delivery_slot": rawData["delivery_slot"],
                "pickup_slot": rawData["pickup_slot"]
            }

            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Order added"}, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def get_orders(request):
    if request.method == 'GET':
        users = OrderTable.objects.all().order_by('-id')
        tojson = users.to_json()
        fromjson = json.loads(tojson)
      
        return JsonResponse({"message": "All orders", "data": fromjson}, safe=False, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def update_status(request):
    if request.method == 'PUT':
        try: 
            id = request.GET.get('id', None)
            data = json.loads(request.body)
            order = OrderTable.objects.get(id=ObjectId(id))
            order.iroing = data['iroing']
            order.deliverd = data['deliverd']
            order.save()
            return JsonResponse({"message": "order updated succes"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def update_quantity(request):
    if request.method == 'PUT':
        try: 
            id = request.GET.get('id', None)
            data = json.loads(request.body)
            order = OrderTable.objects.get(id=ObjectId(id))
            order.product = data['product']
            
            order.save()
            return JsonResponse({"message": "order quantty updated succes"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def get_orders_userid(request, id):
    if request.method == 'GET': 
        users = OrderTable.objects(userid=id).all()
        tojson = users.to_json()
        fromjson = json.loads(tojson)
      
        return JsonResponse({"message": "All orders", "data": fromjson}, safe=False, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def get_order_perticuler(request, id):
    if request.method == 'GET': 
        users = OrderTable.objects(id=ObjectId(id)).first()
        tojson = users.to_json()
        fromjson = json.loads(tojson)
      
        return JsonResponse({"message": "All orders", "data": fromjson}, safe=False, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def delete_order(request, id):
    if request.method == 'DELETE':
        try:
            order = OrderTable.objects.get(id=ObjectId(id))
            order.delete()
            return JsonResponse({"message": "Order deleted successfully"}, status=200)
        except OrderTable.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
    return JsonResponse({"error": "Invalid request method"}, status=405)
