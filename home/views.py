from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def teacher(request):
    return render(request, "home/teacher.html")
