from django.urls import path
from . import views

urlpatterns=[
    path('', views.aqipredictor, name='predict'),
    path('result/', views.formInfo, name='result')
]