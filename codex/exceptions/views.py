from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def error_500(request):
    return render(request, 'error.html')