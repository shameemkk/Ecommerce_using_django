from django.contrib import admin
from django.urls import path
from Products import views
urlpatterns = [
    path('list/', views.products_list_view, name='list'),
    path('details/<pk>', views.product_details_view, name='details'),
    
]
