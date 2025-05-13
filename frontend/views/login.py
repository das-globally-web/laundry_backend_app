import os
from bson import ObjectId
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import User
import random
import requests
def generate_otp():
    return random.randint(1000, 9999)

def send_otp(phone_number, otp):
    url = f"https://2factor.in/API/V1/65780837-b84d-11ee-8cbb-0200cd936042/SMS/+91{phone_number}/{otp}/OTP2"
    response = requests.post(url)
    return response.status_code == 200

def login(request):
    request.session.clear()

    if request.method == "POST":
        phone = request.POST.get("phone")
        user = User.objects(phone_number=phone)
        print(user)
        if user:
            otp = generate_otp()
            request.session["otp"] = str(otp)
            request.session["phone"] = phone
            success = send_otp(phone, otp)
            if not success:
                return render(request, "loginuser.html", {"error": "OTP send failed. Try again."})
            return render(request, "verify_otp.html", {"phone": phone})
        else:
            return redirect('register')
   
    return render(request, "loginuser.html")

def verify_otp(request):
    if request.method == "POST":
        user_input_otp = request.POST.get("otp")
        session_otp = request.session.get("otp")
        if user_input_otp == session_otp:
            phone = request.session.get("phone")
            finduser = User.objects.get(phone_number=phone)
            request.session['phone'] = phone
            request.session['id'] = str(ObjectId(finduser.id))
            request.session['name'] = finduser.name
            request.session['address'] = finduser.current_address
            request.session['isLogin'] = True
            # login success, redirect to home
            return redirect("/")  # make sure `home` is defined in urls
        else:
            return render(request, "verify_otp.html", {"error": "Invalid OTP"})
    return redirect("login")
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        current_address = request.POST.get('current_address')
        existing_user = User.objects(phone_number=phone).first()
        print(name, phone, current_address)

        if existing_user:
            return render(request, 'signup.html', {'error': 'User already exists.'})

        try:
            User(
                name=name,
                phone_number=phone,
                country_code="",  # fill properly if needed
                current_address=current_address,
                profile_pic_url="",
                staff=False
            ).save()
            return redirect('/')  # update with actual route
        except Exception as e:
            return render(request, 'signup.html', {'error': str(e)})
    
    return render(request, 'signup.html')

