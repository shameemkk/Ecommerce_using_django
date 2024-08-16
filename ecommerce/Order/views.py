from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from Order.models import Order,OrderItem,Product

# Create your views here.
def cart_product(request):
    user=request.user
    custemer=user.custemer_profile
    cart_obj, created=Order.objects.get_or_create(
        Owner=custemer,
        Order_status=Order.CART_SATGE
        )    
    context={'cart':cart_obj}
    return render (request,'cart.html',context)
def add_to_cart(request):
    if request.POST:
        user=request.user
        custemer=user.custemer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id') 
        print(product_id)
        cart_obj,created=Order.objects.get_or_create(
            Owner=custemer,
            Order_status=Order.CART_SATGE
        )    
        product=Product.objects.get(pk=product_id)
        ordered_item,created=OrderItem.objects.get_or_create(
            Product=product,
            Owner=cart_obj,
            
        ) 
        if created:
            ordered_item.Quantity=quantity
            ordered_item.save()
        else:
            ordered_item.Quantity=ordered_item.Quantity+quantity
            ordered_item.save()
    return redirect('cart')

def remove_item (request, pk):
    item=OrderItem.objects.get(pk=pk)
    item.delete()
    return redirect('cart')

def checkout(request):
    user=request.user
    custemer=user.custemer_profile
    total=request.POST.get('total')
    cart_obj, created=Order.objects.get_or_create(
        Owner=custemer,
        Order_status=Order.CART_SATGE
        )
    if cart_obj:
        cart_obj.Order_status=Order.ORDER_CONFIRM
        cart_obj.Total_price=total
        cart_obj.save()
    else:
        error_msg="unable to process"
    return redirect('cart')