from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import requests
from geopy.distance import geodesic
from .helpers import get_lat_and_lon
from authentication.models import CustomUser

def home(request):
    return HttpResponse("Hello world")

def allProducts(request):
    # Fetching the current location coordinates of the user
    # Fetch the current city of user from the database
    if not request.user.is_authenticated:
        return redirect('login')
    username = request.user
    # print(username)
    user = CustomUser.objects.get(username=username)
    if user.user_type == 2:
        lat_consumer,lon_consumer = get_lat_and_lon(user)

        all_farmers = list(Farmer.objects.all())
        l = []
        for i in all_farmers:
            lat_farmer,lon_farmer = get_lat_and_lon(i.name,user_type='farmer')
            distance = geodesic((lat_consumer,lon_consumer),(lat_farmer,lon_farmer)).km
            print((distance))
            if distance<1000:
                l.append(i)
        print(l)
        p = []
        for i in range(len(l)):
            crops = Crop.objects.filter(farmer_name=l[i])
            for j in crops:
                p.append(j)
        # products = Crop.objects.all()
    else:
        print("abs")
        p=[]
    return render(request,'sales/allProducts.html',context={'products':p,"user_type" :user.user_type})


# Particular farmer products
def myProducts(request):
    user = CustomUser.objects.get(username=request.user)

    if user.user_type == 1:
        farmer_object = Farmer.objects.get(name = user)
        products = Crop.objects.filter(farmer_name = farmer_object)
        context = {'products':products,"user_type" :user.user_type}
    else:
        redirect('home')
    return render(request, 'sales/myProducts.html',context)


def productDetail(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        user = CustomUser.objects.get(username=request.user)
        product = Crop.objects.get(pk=pk)
        print(f"user type: {user.user_type}")
        context={"product":product,"user_type" :user.user_type}
    except ObjectDoesNotExist:
        context={}

    return render(request, 'sales/productDetail.html',context)
 
# All orders page of a customer
def myOrders(request):
    customer = CustomUser.objects.get(username=request.user)
    user = Customer.objects.get(name=customer)
    orders = Order.objects.filter(customer=user)
    products = Crop.objects.all()
    for order in orders:
        print(order.__dict__.keys())
    # print(orders)
    mylist = zip(orders,products)
    context = {'orders':orders,'user_type':customer.user_type, 'products':products,"mylist":mylist}
    return render(request, 'sales/myOrders.html',context)



# All orders of a particular farmer


def farmerOrders(request):
    user = CustomerUser.objects.get(username=request.user)
    farmer = Farmer.objects.get(farmer_name=user)
    orders = Order.objects.filter(farmer=farmer)
    return render(request,'sales/farmerOrders.html')
    