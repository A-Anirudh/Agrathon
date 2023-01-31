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
    user = CustomUser.objects.get(username=username)
    if user.user_type == 'consumer':
        lat_consumer,lon_consumer = get_lat_and_lon(user)

        # print(lat,lon)

        all_farmers = list(Farmer.objects.all())
        l = []
        for i in all_farmers:
            lat_farmer,lon_farmer = get_lat_and_lon(i.name,user_type='farmer')
            distance = geodesic((lat_consumer,lon_consumer),(lat_farmer,lon_farmer)).km
            # print(type(distance))
            if distance<200:
                l.append(i)
        print(l)
        p = []
        for i in range(len(l)):
            p.append(Crop.objects.get(farmer_name=l[i]))
        # products = Crop.objects.all()
    else:
        p=[]
    return render(request,'sales/allProducts.html',context={'products':p})

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
        product = Crop.objects.get(pk=pk)
        context={"product":product}
    except ObjectDoesNotExist:
        context={}

    return render(request, 'sales/productDetail.html',context)
 
# All orders page


def myOrders(request):
    customer = CustomUser.objects.get(username=request.user)
    user = Customer.objects.get(name=customer)
    orders = Order.objects.filter(customer=user)
    for order in orders:
        print(order.__dict__.keys())
    # print(orders)
    context = {'orders':orders,'user_type':customer.user_type}
    return render(request, 'sales/myOrders.html',context)
