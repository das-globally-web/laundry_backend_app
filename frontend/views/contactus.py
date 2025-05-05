import os
from django.shortcuts import render

def contactUs(request):
    return render(request, 'contact.html')