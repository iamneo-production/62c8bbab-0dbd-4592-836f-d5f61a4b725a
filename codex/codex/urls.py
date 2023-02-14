from django.contrib import admin
from . import views
from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('iris/', include('irisApp.urls')),
    path('user/', views.user, name='user')
]
