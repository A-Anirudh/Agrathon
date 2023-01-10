from django.shortcuts import render, redirect
from .forms import LoginForm, NewUserForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages



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
    form = NewUserForm(request.POST)
    if form.is_valid():
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.save()
        return redirect('login')
    return render(request, 'authentication/new_user.html', {'form': form})


def logout(request):
    if not request.user.is_authenticated:
        return redirect('home')
    auth_logout(request)
    return render(request, 'authentication/logout.html')