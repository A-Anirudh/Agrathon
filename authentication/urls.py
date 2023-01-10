from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('', home, name='home'),
    path('logout/', logout, name='logout'),
    path('new_user/', new_user, name='new_user'),
]