from django.urls import path
from . import views

urlpatterns=[
 
    path('', views.heatwavepredictor, name='predict-heatwave'),
    path('heatwaveresult/', views.predict_heatwave, name='heatwaveresult')
    
]

# Developed By Team Codex
# Credits: Harsh Anand (Github: anand-harsh), Rishit Kumar 