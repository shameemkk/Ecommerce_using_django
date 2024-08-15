from django.urls import path
from Order import views
urlpatterns = [
    path('cart_products/', views.cart_product, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_cart'),
    
]
