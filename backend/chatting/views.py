from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import displayusername
import random

# Create your views here.

def home(request):
    return render(request, "home.html")

def chat(request):
    displaynames = User.objects.values()
    random_id = random.randint(1, 100000000)
    random1 = random.randint(1, 100000000)
    random2 = random.randint(1, 100000000)
    random3 = random.randint(1, 100000000)
    random4 = random.randint(1, 10)
    random_id = abs(random_id*random1-random2*random1+random4*random1)+random4
    return render(request, "chat.html", {"displayusername": displaynames, "id": random_id})

def conv(request, id, user):
    return render(request, "chat.html")

def register(request): 
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("login/")
        
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"register": form})

def login_(request): 
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("user:home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"login": form})

def login_out(request):
    if request.method == "POST":
        logout(request)
        return redirect("user:register")