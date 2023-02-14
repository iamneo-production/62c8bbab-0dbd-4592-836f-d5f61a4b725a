from . import views
from django.urls import path, include
from rest_framework import routers

urlpatterns=[
    path('', views.predictor),
    path('result/', views.formInfo, name=result)
]