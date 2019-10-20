from django.shortcuts import render

# Create your views here.

def index(request):

    if request.user.is_authenticated:
        redirect = 'hhands/landing.html'
    else:
        redirect = 'hhands/index.html'

    return render(request, redirect, {})