from bson import ObjectId
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random
from users.models import User
from .serializers import UserSerializer
import requests

import random

def generate_otp():
    return random.randint(1000, 9999)



def send_otp(phone_number, otp):
    url = f"https://2factor.in/API/V1/65780837-b84d-11ee-8cbb-0200cd936042/SMS/+91{phone_number}/{otp}/OTP2"
    
    response = requests.post(url)
    
    if response.status_code == 200:
        print("OTP sent successfully!")
        return response.json()
    else:
        print("Failed to send OTP.")
        print("Status Code:", response.status_code)
        return None

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "User registered successfully"}, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        tojson = users.to_json()
        fromjson = json.loads(tojson)
      
        return JsonResponse(fromjson, safe=False, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user = User.objects(phone_number=body['number'])
        print(user)
        if user: 
            tojson = user.to_json()
            fromjson = json.loads(tojson)
            otp = generate_otp()
            print(otp)
            response = send_otp(body['number'], otp)
            if response == None:
                return JsonResponse({"error": "Failed to send OTP"}, status=500)
            return JsonResponse({"message": "Login succes", "data": fromjson[0], "otp": otp}, safe=False, status=200)
        else:
            return JsonResponse({"error": "user not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
    
@csrf_exempt
def update_address(request):
    if request.method == 'PUT':
        try:
            body = json.loads(request.body)
            user = User.objects.get(id=body['id'])
            user.current_address = body['address']
            user.save()
            return JsonResponse({"message": "Address updated successfully"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt
def get_user_perticuler(request, id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=ObjectId(id))
            tojson = user.to_json()
            fromjson = json.loads(tojson)
            return JsonResponse({"message": "User found", "data": fromjson}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)