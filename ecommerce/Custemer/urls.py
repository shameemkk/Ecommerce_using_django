from django.contrib import admin
from django.urls import path
from Custemer import views
urlpatterns = [
    path('', views.Home_Page, name='home'),
    path('registraton/', views.custemer_registration, name='register'),
    path('login/', views.custemer_login, name='login'),
    path('logout/', views.signout, name='logout'),
    path('orders/', views.orders, name='orders'),
    
]
