from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

from django.core.exceptions import ObjectDoesNotExist


def home(request):
    return HttpResponse("Hello world")

def allProducts(request):
    if not request.user.is_authenticated:
        return redirect('login')
    products = Crop.objects.all()
    return render(request,'sales/allProducts.html',context={'products':products})

def productDetail(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        product = Crop.objects.get(pk=pk)
        context={"product":product}
    except ObjectDoesNotExist:
        context={}

    return render(request, 'sales/productDetail.html',context)
 