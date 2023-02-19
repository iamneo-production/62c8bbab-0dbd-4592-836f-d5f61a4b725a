from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
import joblib



def home(request):
    return render(request, 'home.html')

def sourcecode(request):
    return render(request, 'source-code.html')

def features(request):
    return render(request, 'features.html')

def team(request):
    return render(request, 'team.html')


