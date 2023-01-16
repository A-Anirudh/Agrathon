from django.shortcuts import render, redirect
from .forms import LoginForm, NewUserForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib import messages

##################

# from django.utils.datastructures import MultiValueDictKeyError
# Import for Customer and Farmer models
from sales.models import Customer, Farmer


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm(request.POST)
    if form.is_valid():
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            print(user)
            auth_login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.WARNING, 'Wrong credentials')
            return render(request, 'authentication/login.html', {'form': form})
        # print(form.cleaned_data)
    else:
        print('Form not valid')
    context = {
        'form': form
    }
    return render(request, 'authentication/login.html',context)

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'authentication/home.html')

def new_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = NewUserForm(request.POST)
    if form.is_valid():
        username = request.POST['username']
        if CustomUser.objects.filter(username=username).exists():
            messages.add_message(request, messages.WARNING, 'User exists')
            return render(request, 'authentication/new_user.html', {'form': form})
        else:
            # is_farmer =  request.POST['farmer'] == "on"
            # is_consumer = request.POST['consumer'] == "on"
            # try:
            #     is_farmer = request.POST['is_farmer'] == "on"
            #     is_farmer = request.POST['is_consumer'] == "on"
            # except MultiValueDictKeyError:
            #     is_farmer = False
            #     is_consumer = False
            user = CustomUser.objects.create_user(request.POST['username'], email=request.POST['email'], password=request.POST['password'],user_type = request.POST["user_type"])
            user.save()

            print(type(request.POST['user_type']))
            # Filling either customer or Farmer model depending on the user's choice
            if (request.POST['user_type']) == '1':
                print("Farmer being saved!!")
                farmer = Farmer.objects.create(name=user,phone_number=request.POST['phone_number'],email=request.POST['email'],city=request.POST['city'])
                farmer.save()
            else:
                customer = Customer.objects.create(name=user,phone_number=request.POST['phone_number'],email=request.POST['email'],city=request.POST['city'])
                customer.save()

            return redirect('login')
    return render(request, 'authentication/new_user.html', {'form': form})


def logout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    auth_logout(request)
    return render(request, 'authentication/logout.html')