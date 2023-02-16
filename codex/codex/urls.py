from django.contrib import admin
from . import views
from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('user/', views.user, name='user'),
    path('form/', views.form, name='form'),
    path('result/', views.result, name='result')
]
