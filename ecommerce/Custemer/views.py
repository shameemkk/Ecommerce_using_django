from django.shortcuts import render
from Products.models import Product

# Create your views here.
def Home_Page(request):
    featured_products=Product.objects.order_by('priority')[:4]
    return render(request,'index.html',{'product':featured_products})
