from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
import joblib



def home(request):
    return render(request, 'home.html')

def user(request):
    username=request.GET['username']
    return render(request, 'user.html', {'name':username})

def form(request):
    return render(request, 'form.html')

