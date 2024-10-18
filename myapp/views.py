from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, 'index.html')

def Shopping_car (request):
    return render (request, 'Shopping_car.html')

def checkout(request):
    return render (request, 'checkout.html')