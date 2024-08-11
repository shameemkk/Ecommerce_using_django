from django.contrib import admin
from django.urls import path
from Custemer import views
urlpatterns = [
    path('', views.Home_Page),
    
]
