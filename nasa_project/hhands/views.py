from django.shortcuts import render

# Create your views here.

def index(request):
    redirect = 'hhands/login.html'
    return render(request, redirect, {})

def app(request):
    return render(request, 'hhands/app.html')