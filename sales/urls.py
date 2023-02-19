from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', allProducts, name='allProducts'),
    path('products/<int:pk>',productDetail, name='productDetail'),
    # Orders for consumer
    path('myOrders/',myOrders, name='myOrders'),
    path('orderConfirm',orderConfirm, name='orderConfirm'),

    #Farmer products
    path('myProducts',myProducts,name='myProducts'),
    path('cart',cart,name='cart'),
    path('orders',farmerOrders,name='farmerOrders')

]