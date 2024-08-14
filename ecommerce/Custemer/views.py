from django.shortcuts import render,redirect
from Products.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from Custemer.models import Custemer

# Create your views here.
def Home_Page(request):
    featured_products=Product.objects.order_by('priority')[:4]
    return render(request,'index.html',{'product':featured_products})

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