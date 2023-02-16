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

def result(request):
    cls=joblib.load("finalized_model.sav")

    lis=[]
    lis.append(request.GET['RI'])
    lis.append(request.GET['Na'])
    lis.append(request.GET['Mg'])
    lis.append(request.GET['Al'])
    lis.append(request.GET['Si'])
    lis.append(request.GET['K'])
    lis.append(request.GET['Ca'])
    lis.append(request.GET['Ba'])
    lis.append(request.GET['Fe'])

    ans=cls.predict([lis])
    print(lis)
    return render(request, 'result.html', {'ans': ans})