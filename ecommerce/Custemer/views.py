from django.shortcuts import render,redirect
from Products.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from Custemer.models import Custemer
from Order.models import Order,OrderItem

# Create your views here.
def Home_Page(request):
    featured_products=Product.objects.order_by('priority')[:4]
    return render(request,'index.html',{'product':featured_products})
def orders(request):
    user=request.user
    custemer=user.custemer_profile
    order_obj=Order.objects.filter(Owner=custemer).exclude(Order_status=Order.CART_SATGE)
    order_items = []
    for order in order_obj:
        order_items.extend(OrderItem.objects.filter(Owner=order))
    products = [item.Product for item in order_items]
    context = {'orders': order_obj, 'products': products , 'OrderItem':order_items}
    
    return render(request,'orders.html',context)

def custemer_registration(request):
    if request.POST:
       try:
            Name=request.POST.get('name')
            Phone=request.POST.get('phone')
            Address=request.POST.get('address')
            Email=request.POST.get('email')
            Password=request.POST.get('password')
            user=User.objects.create_user(
                username=Name,
                email=Email,
                password=Password
            )
            custemer=Custemer.objects.create(
                User=user,
                Name=Name,
                Phone=Phone,
                Address=Address,
            )
            return redirect('login')
       except Exception as e:
        print(e) 
    return render(request,'register.html')

def  custemer_login(request):
   if request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            User=authenticate(request,username=username,password=password)
            if User :
                login(request,User)
                return redirect('home')
            else:
                print("something wrong")
        except Exception as e:
            print(e)
   return render(request,'login.html')
def signout(request):
    logout(request)
    return redirect('home')