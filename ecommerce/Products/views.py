from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def products_list_view(request):
    page=1
    if request.GET:
        page=request.GET('page',1)  
    product_list=Product.objects.all()
    product_paginator=Paginator(product_list,9)
    product_list=product_paginator.get_page(page)
    return render(request,'products.html',{'products':product_list })

def product_details_view(request,pk):
    product_details=Product.objects.get(pk=pk)
    latest_products=Product.objects.order_by('-id')[:4]
    var={
        'product':product_details,
        'latest_products':latest_products
    }
    return render(request,'detailed_product.html',var)