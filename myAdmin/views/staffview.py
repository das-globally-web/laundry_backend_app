import json
from django.shortcuts import render, redirect
from myAdmin.views.decorators import session_login_required
from users.models import User
from users.serializers import UserSerializer  # import serializer
from mongoengine.errors import NotUniqueError
@session_login_required
def addstaff_user(request):
    if request.method == "POST":
        form_data = {
            "name": request.POST.get("name"),
            "phone_number": request.POST.get("phone_number"),
            "country_code": "91",
            "current_address": "test",
            "profile_pic_url": "test",
            "staff": request.POST.get("staff") == "on"
        }

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():
            try:
                serializer.save()
                return redirect("get_staff")
            except NotUniqueError:
                return render(request, "addstaff.html", {"error": "Email or Phone already exists."})
        else:
            return render(request, "addstaff.html", {"error": serializer.errors})

    return render(request, "addstaff.html")


@session_login_required
def get_staff(request):
    if request.method == "GET":
        users = User.objects(staff=True)
        
        return render(request, "staff_list.html", {"users": users})
    return render(request, "staff_list.html", {"error": "Invalid request method"})


from bson import ObjectId

@session_login_required
def editstaff_user(request, id):
    user = User.objects.get(id=ObjectId(str(id)))

    if request.method == "POST":
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.phone_number = request.POST.get("phone_number")
        user.staff = request.POST.get("staff") == "on"
        user.country_code = "91"
        user.current_address = "test"
        user.profile_pic_url = "test"

        try:
            user.save()
            return redirect("get_staff")
        except NotUniqueError:
            return render(request, "addstaff.html", {"error": "Email or Phone already exists.", "user": user})

    return render(request, "addstaff.html", {"user": user})