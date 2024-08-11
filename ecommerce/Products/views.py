from django.shortcuts import render
from .models import Product
# Create your views here.

def products_list_view(request):
    product_list=Product.objects.all()
    return render(request,'products.html',{'products':product_list })