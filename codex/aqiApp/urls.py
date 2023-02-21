from django.urls import path
from . import views

urlpatterns=[
 
    path('', views.aqipredictor, name='predict-aqi'),
    path('result/', views.predict_aqi, name='result')
    
]