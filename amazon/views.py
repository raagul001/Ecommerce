from django.shortcuts import render,redirect
from amazon.form import form_register        # type: ignore
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json

# Create your views here.
def Purchase(request):
    products=Product.objects.filter(Trending=1)
    return render(request,'amazon/index.html',{"products":products})

def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      product_status=Product.objects.get(id=product_id)
      if product_status:
        if Cart.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Cart'}, status=200)
        else:
          if product_status.quantity>=product_qty:
            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)

def Login_page(request):
    if request.user.is_authenticated:
       return redirect("/")
    else:
       if request.method=='POST':
          name=request.POST.get('username')
          password=request.POST.get('password')
          user=authenticate(request,username=name,password=password)
          if user is not None:
             login(request,user)
             messages.success(request,"Logged in Successfully")
             return redirect("/")
          else:
             messages.error(request,"Invalid User Name or Password")
             return redirect("/login")
       return render(request,'amazon/login.html')

def Logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")

def Register(request):
    form=form_register()
    if request.method=='POST':
       form=form_register(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request,"Registration Success You can Login Now..!")
          return redirect('/login')
    return render(request,'amazon/register.html',{"form":form})

def collections(request):
    customer=Customer.objects.filter(Status=0)
    return render(request,'amazon/collections.html',{"customer":customer})

def details(request,name):
     if(Customer.objects.filter(name=name,Status=0)):
      products=Product.objects.filter(customer__name=name)
      return render(request,"amazon/products/index.html",{"products":products,"customer_name":name})
     else:
        messages.warning(request,"No Such Catagory Found")
        return redirect('collections')

def product_details(request,cname,pname):
    if(Customer.objects.filter(name=cname,Status=0)):
      if(Product.objects.filter(name=pname,Status=0)):
        products=Product.objects.filter(name=pname,Status=0).first()
        return render(request,"amazon/products/product_details.html",{"products":products})
      else:
        messages.error(request,"No Such Product Found")
        return redirect('collections')
    else:
      messages.error(request,"No Such Catagory Found")
      return redirect('collections')
    
def cart_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        return render(request, "amazon/cart.html", {"cart": cart})
    else:
        return redirect("/")

def Remove_cart(request,cid):
   cartitem=Cart.objects.get(id=cid)
   cartitem.delete()
   return redirect("/cart")

def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']
      product_status=Product.objects.get(id=product_id)
      if product_status:
         if Favourite.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Favourite'}, status=200)
         else:
          Favourite.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Product Added to Favourite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
   
def favviewpage(request):
  if request.user.is_authenticated:
    fav=Favourite.objects.filter(user=request.user)
    return render(request,"amazon/fav.html",{"fav":fav})
  else:
    return redirect("/")
  
def remove_fav(request,fid):
  x=Favourite.objects.get(id=fid)
  x.delete()
  return redirect("/favviewpage")
 