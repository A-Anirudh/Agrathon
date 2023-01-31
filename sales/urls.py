from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', allProducts, name='allProducts'),
    path('products/<int:pk>',productDetail, name='productDetail'),
    # Orders for consumer
    path('myOrders/',myOrders, name='myOrders'),

    #Farmer products
    path('myProducts',myProducts,name='myProducts'),
]