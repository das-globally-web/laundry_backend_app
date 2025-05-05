import os
from django.shortcuts import render

def service(request):
    return render(request, 'servicees.html')